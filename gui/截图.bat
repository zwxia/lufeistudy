md  ��ͼ
adb shell mkdir /sdcard/jietu/
adb shell screencap /sdcard/jietu/`date +%%Y%%m%%d%%H%%M%%S`.png
adb pull sdcard/jietu/  ��ͼ
adb shell rm -rf /sdcard/jietu