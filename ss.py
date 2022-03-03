import pyautogui
import time
from datetime import datetime
# from drive_upload import Upload
import os
from send_image import SendImage

class Take():
	def __init__(self, u_name, id):
		self.u_name = u_name
		self.id = id

	def take_screenshot(self):
		image_name = f"{self.u_name}"
		myscreen = pyautogui.screenshot()
		cur_path = os.getcwd()
		print(cur_path)
		myscreen.save(f'{image_name}.jpeg')
		print(f'{image_name}.jpeg')
		temp = SendImage(self.id, f'{image_name}.jpeg')
		temp.send()
		# temp = Upload(f'{image_name}.png').drive_upload()
		# os.remove(f'{image_name}.jpg') # Remove photos from local for storage optimization

	def main(self):
		print("Taking screenshot")
		self.take_screenshot()
		# time.sleep(5)