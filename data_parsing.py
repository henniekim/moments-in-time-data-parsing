import glob
import argparse

# Creating a parser
parser = argparse.ArgumentParser()

# Parameter passing from command line : usage - python data_parsing.py source_folder destination_folder 
parser.add_argument("source_folder", type=str, help=" The folder which contains dataset ")
parser.add_argument("destination_folder", type=str, help=" Processed file will be saved here ")
parser.add_argument("--ext", type=str, dest="file_format", help=" File format ")

args = parser.parse_args()

source = args.source_folder
destination = args.destination_folder
format = args.file_format

print(' Dataset are loaded from : '+source)
print(' Processed data will be saved at : '+destination)
print(' Selected file format is : '+format)

vid_list = glob.glob(source+'/*/*.'+format)
num_vid = len(vid_list)
print('The number of training video is : '+str(num_vid))

#for current_vid in range(num_vid):
  # 