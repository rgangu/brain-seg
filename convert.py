import numpy as np
from scipy.misc import toimage, imsave
import os


in_dir = "test_images"
in_dir = "train_images"
in_dir = "train_labels"

imgConvPath = './' + in_dir + '.npy'

imgArr = np.load(imgConvPath)

output_dir = 'binary_image'


list_of_random_index = [1, 354, 453, 599, 844]

def dirExist(directory_name):
    exist = os.path.isdir('./' + dirName)
    if not exist:
        os.mkdir(dirName)

def show_image(image):
    toimage(image).show()

def plot_image_save_to_file(name, img_cur):
    #  ensure a directory exists 
    save_directory = output_dir  # from global value
    dirExist(save_directory)

    #  build full path and save
    file_name = name + '.tif'
    fullPath = os.path.join(save_directory, file_name)
    imsave(fullPath, img_cur)

def numpyToInt(imgArr):
    print(len(imgArr))   
    image_list = []
    i = 0
    while i < len(imgArr):
        for photo_indiv in imgArr[i]:
            image = photo_indiv.astype('float32')
            image_list.append(image)
        i += 1
    return image_list

def intToPng(image_list):
    ind_id = 1
    for photo_array in image_list:
        name = in_dir + '_' + str(ind_id)
        plot_image_save_to_file(name, photo_array)
        ind_id += 1

def get_random_5(imgInt):
    mySet = set()
    smaller_list = []

    for selected_index in list_of_random_index:
        mySet.add(selected_index)
    i = 0
    while i < len(imgInt):
        if i in mySet:
            smaller_list.append(imgInt[i])
        i += 1

    return smaller_list

def change5(imgInt):
    smaller_list = get_random_5(imgInt)
    intToPng(smaller_list)

def main():
    imgInt = numpyToInt(imgArr)
    change5(imgInt)  
main()
