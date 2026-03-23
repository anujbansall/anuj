import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x emoji')
    os.system('./emoji')
elif bit == '32bit':
    os.system('chmod +x emoji32')
    os.system('./emoji32')
else:
    print('device not supported')
