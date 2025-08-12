[app]

# (str) Title of your application
title = تطبيق Kivy إرسال رسالة

# (str) Package name
package.name = kivytelegramapp

# (str) Package domain (reverse domain style)
package.domain = org.example

# (str) Source code directory (ضع نقطة إذا في نفس المجلد)
source.dir = .

# (list) Application requirements
requirements = python3,kivy,requests

# (list) Permissions required by the app
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET, READ_SMS, RECEIVE_SMS

# (bool) Request legacy external storage (مهم للوصول للملفات في أندرويد 10+)
android.requestLegacyExternalStorage = true

# (str) Android API to target
android.api = 33

# (str) Minimum Android API your app will support
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) Use private data storage or public directory (false للسماح بالوصول للملفات في مجلد خارجي)
android.private_storage = false

# (str) Supported orientations
orientation = portrait

# (str) Version name
version = 1.0.0

# (int) Version code (رقم يزيد مع كل تحديث)
version.code = 1

# (str) Icon file (اختياري - ضع مسار أيقونة التطبيق هنا)
# icon.filename = %(source.dir)s/icon.png

# (str) Presplash color (اختياري)
# presplash.color = #FFFFFF

[buildozer]

# (int) Logging level (0=debug, 1=info, 2=warning, 3=error)
log_level = 2

# (bool) Warn if run as root
warn_on_root = 1
