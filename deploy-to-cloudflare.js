const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

// รับพารามิเตอร์ชื่อโฟลเดอร์แอป (เช่น kongsuk-agri-drone)
const appName = process.argv[2] || 'kongsuk-agri-drone';
const appPath = path.join(__dirname, appName);

if (!fs.existsSync(appPath)) {
  console.error(`❌ ไม่พบโฟลเดอร์แอปเป้าหมาย: ${appPath}`);
  process.exit(1);
}

console.log(`🚀 เริ่มต้นกระบวนการดีพลอยแอป "${appName}" ขึ้น Cloudflare & GitHub...`);

// ฟังก์ชันรันคำสั่งพร้อมซ่อนหน้าต่างดำ (windowsHide)
function runCmd(cmd, cwd = __dirname) {
  console.log(`💻 รันคำสั่ง: ${cmd}`);
  try {
    const stdout = execSync(cmd, { cwd, encoding: 'utf8', windowsHide: true });
    if (stdout && stdout.trim()) console.log(stdout.trim());
    return true;
  } catch (err) {
    console.error(`❌ เกิดข้อผิดพลาดในการรันคำสั่ง: ${err.message}`);
    if (err.stdout) console.log(err.stdout);
    if (err.stderr) console.error(err.stderr);
    return false;
  }
}

// 1. ตรวจสอบและเตรียม Git ในโฟลเดอร์ kongsuk-apps
const hasGit = fs.existsSync(path.join(__dirname, '.git'));
if (!hasGit) {
  console.log('📌 ยังไม่ได้ทำ Git init ใน kongsuk-apps — เริ่มต้นตั้งค่า Git...');
  runCmd('git init');
  runCmd('git branch -M main');
}

// 2. ดำเนินการอัปโหลดโค้ดขึ้น GitHub (Git Push)
console.log('\n📦 [ขั้นตอนที่ 1] ทำการ Commit และ Push โค้ดทั้งหมดขึ้น GitHub...');
runCmd('git add .');
// ตรวจสอบสถานะการเปลี่ยนแปลง
const status = execSync('git status --porcelain', { encoding: 'utf8', windowsHide: true });
if (status.trim()) {
  const commitMsg = `Auto deploy ${appName} to Cloudflare and GitHub - ${new Date().toISOString()}`;
  runCmd(`git commit -m "${commitMsg}"`);
  
  // เช็คว่ามี remote origin หรือไม่
  try {
    const remote = execSync('git remote get-url origin', { encoding: 'utf8', windowsHide: true }).trim();
    if (remote) {
      console.log(`📡 พบ Remote GitHub: ${remote}`);
      runCmd('git push -u origin main');
    }
  } catch (e) {
    console.warn('⚠️ ไม่พบ Remote 'origin' ของ GitHub — กรุณาพิมพ์สั่งเชื่อมต่อ Remote ก่อน เพื่อผลักดันโค้ดขึ้น GitHub');
    console.warn('   (ตัวอย่าง: git remote add origin https://github.com/Chayapong/YOUR_REPO.git)');
  }
} else {
  console.log('🟢 ไม่มีโค้ดแอปเปลี่ยนแปลงใน Git — ข้ามขั้นตอน Commit & Push');
}

// 3. ดำเนินการดีพลอยขึ้น Cloudflare Pages ด้วย Wrangler
console.log('\n⛅️ [ขั้นตอนที่ 2] กำลังดีพลอยแอปขึ้น Cloudflare Pages...');
// ชี้ให้ wrangler ดีพลอยโฟลเดอร์แอปนั้นๆ โดยกำหนดชื่อโปรเจกต์ให้ตรงกับชื่อโฟลเดอร์
const wranglerCmd = `npx wrangler pages deploy "${appPath}" --project-name "${appName}"`;
const deploySuccess = runCmd(wranglerCmd);

if (deploySuccess) {
  console.log(`\n🎉 ดีพลอยและส่งโค้ดขึ้น GitHub สำหรับแอป "${appName}" สำเร็จเสร็จสิ้นเรียบร้อยแล้ว!`);
} else {
  console.error('\n❌ การดีพลอยขึ้น Cloudflare Pages ล้มเหลว กรุณาตรวจสอบข้อความความผิดพลาดด้านบน');
}
