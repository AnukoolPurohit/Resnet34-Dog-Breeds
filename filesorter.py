import csv
import os


SOURCE_ROOT = 'train'
DEST_ROOT = 'train2'


with open('labels.csv') as infile:
	next(infile)	# Skip the header row
	reader = csv.reader(infile)
	seen = set()
	for dogid, breed in reader:
		# Create a new directory if needed
		if breed not in seen:
			os.mkdir(os.path.join(DEST_ROOT, breed))
			seen.add(breed)


		src = os.path.join(SOURCE_ROOT, dogid + '.jpg')
		dest = os.path.join(DEST_ROOT, breed, dogid + '.jpg')

		try:
			os.rename(src,dest)
		except WindowsError as e:
			print(e)
