import glob
import argparse
import cv2
import numpy as np

# Creating a parser
parser = argparse.ArgumentParser()

# Parameter passing from command line : usage - python data_parsing.py source_folder destination_folder 
parser.add_argument("source_folder", type=str, help=" The folder which contains dataset ")
parser.add_argument("destination_folder", type=str, help=" Processed file will be saved here ")
parser.add_argument("--ext", type=str, dest="file_format", help=" File format ")
parser.add_argument("training_info", type=str, help=" Training data information file (.csv) ")
parser.add_argument("validation_info", type=str, help=" Validation data information file (.csv) ")

args = parser.parse_args()

source = args.source_folder
destination = args.destination_folder
format = args.file_format
csv_training = args.training_info
csv_validation = args.validation_info

print(' Dataset are loaded from : '+source)
print(' Processed data will be saved at : '+destination)
print(' Selected file format is : '+format)
print(' TrainingSet information is loaded at : '+csv_training)
print(' ValidationSet information is loaded at : '+csv_validation)

vid_list = glob.glob(source+'/*/*.'+format)
num_vid = len(vid_list)
print('The number of training video is : '+str(num_vid))

# Load information from csv (the file is supported by data provider)
training_filename = np.genfromtxt(csv_training, delimiter=',', usecols=0, dtype=None, encoding='utf-8')
training_label = np.genfromtxt(csv_training, delimiter=',', usecols=1, dtype=None, encoding='utf-8')

validation_filename = np.genfromtxt(csv_validation, delimiter=',', dtype=None, encoding='utf-8')
validation_label = np.genfromtxt(csv_validation, delimiter=',', usecols=1, dtype=None, encoding='utf-8')

#print(str(trainingSet))

print(training_filename[0])


# Load video 
#for current_vid in range(num_vid):
#  current_cap = cv2.VideoCapture(source