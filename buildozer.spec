[app]

# (str) Title of your application
title = تطبيق Kivy إرسال رسالة

# (str) Package name
package.name = kivytelegramapp

# (str) Package domain (reverse domain style)
package.domain = org.example

# (str) Source code where the main.py is located
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,requests

# (str) Entry point of the application
# Default is main.py, إذا غيرته غيّر هنا
# entrypoint = main.py

# (list) Permissions required by the app
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET, READ_SMS, RECEIVE_SMS

# (bool) Request legacy external storage (للسماح بالوصول للملفات في اندرويد 10 وما فوق)
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

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = false

# (str) Supported orientations
orientation = portrait

# (bool) Copy icons and splash images into APK (if لديك أيقونات)
# icon.filename = %(source.dir)s/icon.png

# (bool) Copy splash image
# presplash.filename = %(source.dir)s/splash.png

# (list) Garden requirements (إن لم تستخدم فلا تكتب)
# garden_requirements = 

# (str) Presplash color (hex)
# presplash.color = #FFFFFF

# (str) Version code (integer)
version.code = 1

# (str) Version name
version = 1.0.0

---

[buildozer]

log_level = 2
warn_on_root = 1