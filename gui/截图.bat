md  НиЭМ
adb shell mkdir /sdcard/jietu/
adb shell screencap /sdcard/jietu/`date +%%Y%%m%%d%%H%%M%%S`.png
adb pull sdcard/jietu/  НиЭМ
adb shell rm -rf /sdcard/jietu