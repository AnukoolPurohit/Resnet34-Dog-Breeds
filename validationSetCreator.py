import os

SOURCE_ROOT = 'train'
DEST_ROOT = 'valid'


for drc in os.listdir(SOURCE_ROOT):
	os.mkdir(os.path.join(DEST_ROOT, drc))
	for f_name in os.listdir(os.path.join(SOURCE_ROOT, drc))[:10]:
		src = os.path.join(SOURCE_ROOT, drc, f_name)
		dst = os.path.join(DEST_ROOT, drc,f_name)
		try:
			os.rename(src,dst)
		except WindowsError as e:
			print(e)
