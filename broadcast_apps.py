# -*- coding: utf-8 -*-
import urllib.request
import json
import os

TELEGRAM_TOKEN = "8295465995:AAFAKBaVf-Uv2Pf5IutHlPd27T5wfQq7Hvs"
CHAT_ID = "7572179751"

# รายการแอปพรีเมียมระบบกองสุข
apps = [
    {"name": "Kongsuk Agri Drone 🌾", "desc": "ระบบควบคุมและวิเคราะห์พื้นที่โดรนเกษตรอัจฉริยะ", "url": "https://kongsuk-agri-drone.pages.dev"},
    {"name": "Kongsuk AI Streamer 🤖", "desc": "ระบบผู้ประกาศข่าวและสตรีมเมอร์ AI กองสุข", "url": "https://kongsuk-ai-streamer.pages.dev"},
    {"name": "Kongsuk Cashflow Analyzer 💵", "desc": "แดชบอร์ดวิเคราะห์งบการเงินและกระแสเงินสดธุรกิจ", "url": "https://kongsuk-cashflow-analyzer.pages.dev"},
    {"name": "Kongsuk Empire Hub 🏰", "desc": "ศูนย์รวมการควบคุมแดชบอร์ดเครือข่ายกองสุข Empire", "url": "https://kongsuk-empire-hub.pages.dev"},
    {"name": "Kongsuk Mushroom Climate 🍄", "desc": "ระบบมอนิเตอร์และปรับสภาวะโรงเพาะเห็ดอัจฉริยะ", "url": "https://kongsuk-mushroom-climate.pages.dev"},
    {"name": "Kongsuk Smart Air & PM2.5 💨", "desc": "ระบบเกณฑ์และแนะนำปรับตัวฝุ่นละออง AQI รายวัน", "url": "https://kongsuk-smart-air.pages.dev"},
    {"name": "Kongsuk Smartfarm Monitor 🚜", "desc": "แดชบอร์ดตรวจวัดสถานะโรงเรือนฟาร์มอัจฉริยะ", "url": "https://kongsuk-smartfarm-monitor.pages.dev"},
    {"name": "Kongsuk Soil Moisture Smart Calculator 💧", "desc": "ระบบคำนวณและตั้งเซนเซอร์วัดดินแห้ง-เปียก", "url": "https://kongsuk-soil-moisture-calculator.pages.dev"},
    {"name": "Kongsuk Trading Dashboard 📊", "desc": "แดชบอร์ดรายงานผลสุขภาพพอร์ตสถิติซื้อขายออโต้", "url": "https://kongsuk-trading-dashboard.pages.dev"},
    {"name": "Kongsuk AI VTuber Live Commerce & Inventory Simulator 🛒", "desc": "ระบบจำลองสตรีมสด AI VTuber และจัดการคลังสินค้าอัจฉริยะ", "url": "https://kongsuk-live-commerce-inventory.pages.dev"}
]

# สร้างข้อความสำหรับ Telegram
msg = "📢 <b>[ประชาสัมพันธ์] แอปพรีเมียมระบบกองสุข ออนไลน์เรียบร้อย!</b>\n\n"
msg += "บัดนี้ ทีมเอเจนท์ได้ดำเนินการอัปโหลดและเปิดใช้งาน (Deploy) SaaS Web Apps พรีเมียมระบบกระจก Glassmorphism Glow ทั้งหมด 9 แอปหลัก ขึ้นบนคลาวด์ <b>Cloudflare Pages</b> และสำรองโค้ดสู่ <b>GitHub</b> เรียบร้อยแล้วครับ!\n\n"
msg += "📋 <b>รายชื่อแอปออนไลน์ปัจจุบัน:</b>\n"

for i, app in enumerate(apps, 1):
    msg += f" {i}. <b>{app['name']}</b>\n"
    msg += f"   - {app['desc']}\n"
    msg += f"   - 🌎 Link: <a href='{app['url']}'>{app['url']}</a>\n\n"

msg += "📦 <b>GitHub Repository:</b> <a href='https://github.com/paitoolr/ai-customer-support.git'>paitoolr/ai-customer-support</a>\n"
msg += "📈 <i>ยอดความสำเร็จหมวดพัฒนา Premium App สะสมขยับขึ้นนำระบบ 100%</i>"

# ยิงรายงานเข้า Telegram
url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": msg,
    "parse_mode": "HTML",
    "disable_web_page_preview": True
}
req = urllib.request.Request(
    url, 
    data=json.dumps(data).encode('utf-8'), 
    headers={'Content-Type': 'application/json'}
)

try:
    with urllib.request.urlopen(req) as response:
        res = response.read().decode('utf-8')
        print("Telegram broadcast success:", res)
except Exception as e:
    print("Telegram broadcast failed:", str(e))

# เขียนบันทึกรายงานใส่สมอง (cloudflare_apps_report.md)
brain_dir = r"C:\Users\Administrator\.gemini\antigravity-cli\brain\e70fc94f-b213-4ddd-a7a7-96f786732090"
report_path = os.path.join(brain_dir, "cloudflare_apps_report.md")

md_content = """# ☁️ รายงานสารบัญแอปพรีเมียมระบบกองสุขบน Cloudflare Pages & GitHub
*อัปเดตสถานะล่าสุดเมื่อ: 14 มิถุนายน 2026*

บัดนี้ระบบกองสุขได้พัฒนาและดีพลอยเปิดใช้งาน SaaS Web Apps พรีเมียมสำเร็จลุล่วงและเชื่อมต่อออนไลน์แบบสมบูรณ์บนโครงสร้าง Cloudflare Pages & GitHub ดังมีรายละเอียดดังนี้:

---

## 🗂️ รายชื่อแอปพรีเมียมออนแอร์เรียบร้อย (9 แอปหลัก)

"""

for i, app in enumerate(apps, 1):
    md_content += f"### {i}. {app['name']}\n"
    md_content += f"*   **รายละเอียด:** {app['desc']}\n"
    md_content += f"*   **ลิงก์ดีพลอยจริง:** [{app['url']}]({app['url']})\n"
    md_content += f"*   **ที่เก็บซอร์สโค้ด:** [GitHub Repository](https://github.com/paitoolr/ai-customer-support.git)\n\n"

md_content += """---
*บันทึกข้อมูลส่วนสมอง: Antigravity AI Agent*
"""

with open(report_path, "w", encoding="utf-8") as f:
    f.write(md_content)
print("Saved brain artifact: cloudflare_apps_report.md")
