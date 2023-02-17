import random


class Task():
	def __init__(self, time):
		"""Initializing the task"""
		self.timestamp = time
		self.pages = random.randrange(1, 21)

	def get_stamp(self):
		"""Returns task timestamp"""
		return self.timestamp
	def get_pages(self):
		"""Returns task no.of pages"""
		return self.pages

	def wait_time(self, current_time):
		"""returns  the wait time of a task"""
		wait_time = current_time - self.timestamp
		return wait_time