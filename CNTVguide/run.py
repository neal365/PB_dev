import os,sys
IP = '192.168.10.106'

if( sys.argv[1] == 'r' ):
	print "reinstall app:"
	os.system(r'blackberry-deploy -installApp -password qqww  -device ' + IP + r' -package "bin\CNTVguide.bar" -launchApp')
	sys.exit()
		
input = open('version.txt', 'r')
version = input.readline()
msg = 'build version is ' + version
version = int(version)
print msg

print "zip the package"
os.system(r"del CNTVguide.zip")
os.system(r'"C:\Program Files (x86)\WinZip\wzzip.exe"  CNTVguide.zip config.xml index.htm logo.png')
print "package to bar and sign"
command = r'bbwp "CNTVguide.zip" -gcsk Playbook123 -gp12 Playbook123 -buildId ' + str(version+1)
os.system(command)
print "install bar"
os.system(r'blackberry-deploy -uninstallApp -password qqww  -device ' + IP + r' -package "bin\CNTVguide.bar" ')
os.system(r'blackberry-deploy -installApp -password qqww  -device ' + IP + r' -package "bin\CNTVguide.bar" -launchApp')
input.close()
input = open('version.txt', 'w')
input.write(str(version+1))
input.close()
