#Library
from PIL import Image
import os
import utils


class NanoNetsImage:
	def __init__(self, img_location):
		self.image_name = os.path.split(img_location)[-1]
		self.image = self.validate_img(img_location)

	def validate_img(self, image):
		try:
			img = Image.open(image)
			return img
		except IOError as e:
			print e.message
			print("File %s is not a valid image" % image)
			img = None
			raise e

	def convert(self):
		if self.image != None: 
			self.image = self.image.convert('RGB')

	def resize(self, target_size):
		# Rsizes the image and saves in the new path
		if self.image != None:
			self.image =  self.image.resize((target_size, target_size), Image.ANTIALIAS)

	def save(self, out_dir, filename):
		try:
			if self.image != None:
				utils.check_and_mkdir(out_dir)
				self.image.save(out_dir + "/" + filename)
				print("File %s saved at %s/%s" %(filename, out_dir, filename))
		except Exception as e:
			print e.message


