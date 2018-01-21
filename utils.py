import os
import yaml

CONFIG = yaml.load(open("config.yml", 'r'))

def check_and_mkdir(dir_path):
	if not os.path.exists(dir_path):
			print("Creating "+ dir_path + "\n")
			os.makedirs(dir_path)


def get_images(dir):
	files = (file for file in os.listdir(dir) 
         if os.path.isfile(os.path.join(dir, file)))
	return files

def get_categories(path):
	if os.path.exists(path):
		categories = [x[1] for x in os.walk(path)][0]
		return [os.path.join(path, s) for s in categories]
	else:
		raise OSError(2, 'No such file or directory', path)



def split_dataset(images):
	total_images = len(images)
	if total_images!=0:
		training_size = int(total_images*(CONFIG["TRAINING_DATA_SIZE"]/10.0))
		test_size = int(total_images*(CONFIG["TEST_DATA_SIZE"]/10.0))
		training_images = images[0:training_size]
		test_images = images[training_size:training_size+test_size]
		validation_images = images[training_size+test_size:-1]
		data =  { "training": training_images, "test": test_images, "validation": validation_images}
		return data

	