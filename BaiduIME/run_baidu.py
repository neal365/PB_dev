import os
IP = '169.254.0.1'

input = open('version.txt', 'r')
version = input.readline()
msg = 'build version is ' + version
version = int(version)
print msg

print "zip the package"
os.system(r"del BaiduIME.zip")
os.system(r'"C:\Program Files (x86)\WinZip\wzzip.exe"  BaiduIME.zip index_baidu.html config.xml icon_baidu.png bdime_open.js')
print "package to bar and sign"
command = r'bbwp "BaiduIME.zip" -gcsk Playbook123 -gp12 Playbook123 -buildId ' + str(version+1)
os.system(command)
print "install bar"
os.system(r'blackberry-deploy -uninstallApp -password qqww  -device ' + IP + r' -package "bin\BaiduIME.bar" ')
os.system(r'blackberry-deploy -installApp -password qqww  -device ' + IP + r' -package "bin\BaiduIME.bar" -launchApp')
input.close()
input = open('version.txt', 'w')
input.write(str(version+1))
input.close()
