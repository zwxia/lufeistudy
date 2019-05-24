@echo off


echo [*] log截取中，请在该批处理所在文件夹查看log_时间命名的文件
echo [*] 关闭当前页面停止log截取
set yy=%date:~0,4%
set mm=%date:~5,2%
set dd=%date:~8,2%
set hh=%time:~0,2%
set mn=%time:~3,2%
set ss=%time:~6,2%

adb logcat -v threadtime > log_%yy%%mm%%dd%%hh%%mn%%ss%.txt


exit