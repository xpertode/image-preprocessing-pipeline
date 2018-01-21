# README
The script preprocesses the images in input directory and creates a training, test and validation dataset in each category of the dataset and prints the number of images successfully processed in the end.

*Usage: python main.py <input_dataset_location> <output_dataset_location>*

Following settings can be tweaked in the config.yml file as per the requirements:
IMG_TARGET_SIZE,
TRAINING_DATA_SIZE,
TEST_DATA_SIZE,
VALIDATION_DATA_SIZE

#TODO: 
1. Multi threaded processing.
2. Download and upload datasets to some central service.
3. Real time progress of data processed with types of images processed and errors encountered.