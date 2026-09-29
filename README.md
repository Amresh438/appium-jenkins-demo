# Appium + Jenkins Learning Demo

Tests the Android **Settings** app (no APK needed).

## Flow
GitHub (code) -> Jenkins (pulls code) -> Appium (controls phone) -> Report

## Requirements on your machine
- Python 3.9+
- Node.js + Appium 2:  npm install -g appium
- Appium driver:       appium driver install uiautomator2
- Android Studio (SDK + emulator) or a real Android phone with USB debugging ON
- ANDROID_HOME set, and platform-tools (adb) in PATH

## Run locally first (always do this before Jenkins)
1. Start emulator / connect phone. Check:  adb devices
2. Terminal 1:  appium
3. Terminal 2:
     pip install -r requirements.txt
     pytest tests -v

## Run in Jenkins
See the steps given in chat: create a Pipeline job -> "Pipeline script from SCM"
-> your GitHub repo URL -> Script Path: Jenkinsfile -> Build Now.
Appium server and the emulator/phone must be running on the Jenkins machine.
