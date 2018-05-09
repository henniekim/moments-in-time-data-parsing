# Project started 09. May. 2018
# Moments in Time Mini Dataset parser
# Dong Hyun Kim @ Sogang Univ.

import glob
import argparse
import cv2
import numpy as np
import os

# Creating a parser
parser = argparse.ArgumentParser()

# Parameter passing from command line : usage - python data_parsing.py source_folder destination_folder 
parser.add_argument("source_folder", type=str, help=" The folder which contains dataset ")
parser.add_argument("destination_folder", type=str, help=" Processed file will be saved here ")
parser.add_argument("--ext", type=str, dest="file_format", help=" File format ")
parser.add_argument("training_info", type=str, help=" Training data information file (.csv) ")
parser.add_argument("validation_info", type=str, help=" Validation data information file (.csv) ")
parser.add_argument("categories", type=str, help=" Category file (.txt)")
parser.add_argument("--mode", type=str, dest="mode", help=" Choose operation mode ")

args = parser.parse_args()

source = args.source_folder
destination = args.destination_folder
format = args.file_format
csv_training = args.training_info
csv_validation = args.validation_info
txt_category = args.categories
mode = args.mode

print(' Dataset are loaded from : '+source)
print(' Processed data will be saved at : '+destination)
print(' Selected file format is : '+format)
print(' TrainingSet information is loaded at : '+csv_training)
print(' ValidationSet information is loaded at : '+csv_validation)
print(' Category file is loaded at :'+txt_category)

vid_list = glob.glob(source+'/*/*.'+format)
num_vid = len(vid_list)

# load categories from data
category_name = np.loadtxt(txt_category, delimiter=',', usecols=0, dtype=str, encoding='utf-8')
category_encoding = np.loadtxt(txt_category, delimiter=',', usecols=1, dtype=None, encoding='utf-8')

print('The number of training video is : '+str(num_vid))
print('The number of categories is : '+str(len(category_encoding)))

# Load information from csv (the file is supported by data provider)
training_filename = np.genfromtxt(csv_training, delimiter=',', usecols=0, dtype=None, encoding='utf-8')
training_label = np.genfromtxt(csv_training, delimiter=',', usecols=1, dtype=None, encoding='utf-8')

validation_filename = np.genfromtxt(csv_validation, delimiter=',', usecols=0, dtype=None, encoding='utf-8')
validation_label = np.genfromtxt(csv_validation, delimiter=',', usecols=1, dtype=None, encoding='utf-8')

#print(str(trainingSet))

print(training_filename[0])
print(category_name[0])

# Mode select
# mp4 -> jpg
if mode == 'getframe' :
    for current_vid_number in range(num_vid):
        count = 0
        current_vid = cv2.VideoCapture(source+'/'+training_filename[current_vid_number])
        if os.path.isdir(destination + '/' + training_filename[current_vid_number]) == False:
            os.makedirs(destination + '/' + training_filename[current_vid_number])

        while True :
            success, current_frame = current_vid.read()
            if not success:
                break

            if count < 10 :
                str_count = '0'+str(count)
            else :
                str_count = str(count)

            cv2.imwrite(destination+'/'+training_filename[current_vid_number]+'/'+str_count+'.jpg', current_frame)
            count += 1
        print(str(current_vid_number)+'/'+str(num_vid)+'::'+str(count)+' images are extracted in : '+destination+'/'+training_filename[current_vid_number])



# Load video 
#for current_vid in range(num_vid):
#  current_cap = cv2.VideoCapture(source