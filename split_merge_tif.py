from libtiff import TIFF3D,TIFF
dirtype = ("train","label","test")

def splitImg():

	for t in dirtype:
		imgdir = TIFF3D.open(t + "-volume.tif")
		imgarr = imgdir.read_image()
		for i in range(imgarr.shape[0]):
			imgname = t + "/" + str(i) + ".tif"
			img = TIFF.open(imgname,'w')
			img.write_image(imgarr[i])

def mergeImg():

	path = 'C:\Users\rohit\Desktop\Brown\Brain\brain\brainimp'
	imgarr = []
	for i in range(30):
		img = TIFF.open(path + str(i) + ".tif")
		imgarr.append(img.readImg())
	imgdir.writeImg(imgarr)

if __name__ == "__main__":

	merge_img()

