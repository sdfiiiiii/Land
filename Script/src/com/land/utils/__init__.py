 # -*- coding:gb2312 -*- �������ڵ�һ�л��ߵڶ���
import string, os, sys
import tarfile, zipfile
import bz2

"""
dir = 'D:\һЩ����'
print '----------- no sub dir'

files = os.listdir(dir)
for f in files:
    print dir + os.sep + f

print '----------- all dir'

for root, dirs, files in os.walk(dir):
    for name in files:
        print os.path.join(root, name)
"""


eclipse_path = ""
plugin_path = ""
#while True:
#    eclipse_path = raw_input("������eclipse��Ŀ¼��\n")
#    isExist = os.path.exists(eclipse_path)
#    if isExist:
#        break
#    else:
#        print "\tĿ¼" + eclipse_path + "������!\n"
#while True:
#    plugin_path = raw_input("������ ��� ��Ŀ¼��\n")
#    isExist = os.path.exists(plugin_path)
#    if isExist:
#        break
#    else:
#        print "\tĿ¼" + plugin_path + "������!\n"

"""
#ѹ���ļ���Ϊ .tar.bz2
archive = tarfile.open('myarchive.tar.bz2','w:bz2')
archive.debug = 1           # Display the files beeing compressed.
archive.add(r'd:\myfiles')  # d:\myfiles contains the files to compress
archive.close()
"""


#��ѹһ��.tar.bz2
plugin_path = 'D:\һЩ����\php-5.5.4.tar.bz2'
archive = tarfile.open(plugin_path,'r:bz2')
archive.debug = 1    # Display the files beeing decompressed.
for tarinfo in archive:
    archive.extract(tarinfo, r'd:\mydirectory') # d:\mydirectory is where I want to uncompress the files.
archive.close()

zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), 'txt.zip'))
for file in zipFile.namelist():
    zipFile.extract(file, r'd:/Work')
zipFile.close()

to be continue










