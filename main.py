# file transfer script

import os
import shutil
import sys


if len(sys.argv) < 2:
	print("\n\nPlease enter camera model after file name when executing this script.\n\n")
	exit()

canon = False
fuji = False
test = False

if sys.argv[1] == "canon":
	canon = True
if sys.argv[1] == "fuji101":
	fuji101 = True
if sys.argv[1] == "fuji102":
	fuji102 = True

# build list of local jpegs
file_list  = os.listdir(os.getcwd())
fuji_path_101 = "/Volumes/EOS_DIGITAL/DCIM/101_FUJI/"
fuji_path_202 = "/Volumes/EOS_DIGITAL/DCIM/102_FUJI/"
fuji_ext = ".RAF"
canon_path = "/Volumes/EOS_DIGITAL/DCIM/100CANON/"
canon_ext = ".CR3"
test_path = "/Volumes/ESD-USB/sources/"
test_ext = ".gif"

pic_names = list()

for f in file_list:
	if (".JPEG" in f):
		pic_names.append(f.replace(".JPEG",""))
	if (".JPG" in f):
		pic_names.append(f.replace(".JPG",""))
	if (".jpeg" in f):
		pic_names.append(f.replace(".jpeg",""))
	if (".jpg" in f):
		pic_names.append(f.replace(".jpg",""))


# iterate through file name list and copy raw to local folder

if fuji101:
	path = fuji_path_101
	ext = fuji_ext
if fuji102:
	path = fuji_path_102
	ext = fuji_ext
if canon:
	path = canon_path
	ext = canon_ext
#if test:
#	path = test_path
#	ext = test_ext
if not (fuji or canon or test):
	print("\nPlease type: 'python copy_pics.py fuji' or 'python copy_pics.py canon' to execute script\n")
	exit()

for p in pic_names:
	print("Preparing to copy "+path+p+ext+" to "+os.getcwd())
	try:
		shutil.copy2(path+p+ext, os.getcwd())
		print("Success.")
	except (IOError):
		print("\n\t"+path+p+ext+" was not found.\n")
