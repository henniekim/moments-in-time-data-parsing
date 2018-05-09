# moments-in-time-data-parsing #
This repository is to parse data from Moments in Times Dataset
Moments in Times Dataset consists of 100,000 videos. Each video lasts 3sec(about 90 frames) 

## Dependencies
python 3.6.4, Opencv 3.x are needed.
Virtual environment is recommended!

## Data
You can download moments in Time dataset from 
> http://moments.csail.mit.edu/

## Usage 
1. Command line (sorry for long arguments)
```sh
python data_parsing.py [source_folder] [detination_folder] --ext mp4 [trainingSet_source] [validationSet_source] [categories_source] --mode getframe
```
2. Scripts (recommended)
Fix given script file named "data_parsing.sh", if you don't want to type such a long command as above

## Updates
* 0.0.1
  * Frame extractor added

## Contacts

김동현 (Dong Hyun Kim) - seru_s@me.com

## License
MIT @ henniekim
