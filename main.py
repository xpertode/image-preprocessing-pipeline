
import yaml
from nanonetsimage import NanoNetsImage
import sys
import os
import random
import utils

CONFIG = yaml.load(open("config.yml", 'r'))

def preprocess_image(path, img, save_to):
	image_path = os.path.join(path, img)
	try:
		print "Processing image " + image_path
		im = NanoNetsImage(image_path)
		im.convert
		im.resize(CONFIG["IMG_TARGET_SIZE"])
		im.save(save_to, img)
		return 0
	except Exception as e:
		print "Failed to process " + image_path + ": " + e.message
		return 1


if __name__ == "__main__":
	if sys.argv < 2:
		print "Usage: python main.py <input_location> <output_location>\n"
		sys.exit(0)

	dataset_path = sys.argv[1]
	output_path = sys.argv[2]

	categories = utils.get_categories(dataset_path)
	total = 0
	success = 0
	for category in categories:
		category_name = category.split("/")[-1]
		print "Processing category " + category
		images = utils.get_images(category)
		images = list(images)
		random.shuffle(images)
		
		data = utils.split_dataset(images)
		for data_type, image_data in data.iteritems():
			save_to = os.path.join(output_path, category_name, data_type)
			total += len(image_data)
			for img in image_data:
				status = preprocess_image(category, img, save_to)
				if status == 0:
					success += 1
	success_rate = (float(success)/total)*100
	print("Succesfully processed %d/%d (%.2f%%) images.\n" % (success, total, success_rate))
		
		





