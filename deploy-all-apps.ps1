$apps = @(
  "kongsuk-agri-drone",
  "kongsuk-ai-streamer",
  "kongsuk-cashflow-analyzer",
  "kongsuk-empire-hub",
  "kongsuk-mushroom-climate",
  "kongsuk-smart-air",
  "kongsuk-smartfarm-monitor",
  "kongsuk-soil-moisture-calculator",
  "kongsuk-trading-dashboard",
  "kongsuk-live-commerce-inventory"
)

$DIR = "C:\Users\Administrator\kongsuk-apps"
Set-Location $DIR

# 1. สร้างโปรเจกต์ Cloudflare Pages (หากยังไม่มี)
foreach ($app in $apps) {
  Write-Host "⛅️ Checking/Creating Cloudflare Project: $app"
  & npx wrangler pages project create "$app" --production-branch main 2>&1 | Out-Null
}

# 2. ดีพลอยทุกตัวขึ้น Cloudflare Pages
foreach ($app in $apps) {
  Write-Host "🚀 Deploying to Cloudflare Pages: $app"
  & npx wrangler pages deploy "$DIR\$app" --project-name "$app"
}

# 3. ผลักดันขึ้น GitHub
Write-Host "📦 Git add, commit and push to GitHub..."
git add .
$status = git status --porcelain
if ($status) {
  $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
  git commit -m "Auto deploy and sync all kongsuk apps - $date"
  git push origin main
} else {
  Write-Host "🟢 No changes to push."
}

Write-Host "🎉 [SUCCESS] All apps are deployed to Cloudflare and pushed to GitHub!"
