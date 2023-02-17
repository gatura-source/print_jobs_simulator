"""Simulating printing tasks"""
# A more interesting simulation allows us to study the behavior of the printing queue described
# earlier in this section. Recall that as students send printing tasks to the shared printer, the tasks
# are placed in a queue to be processed in a first-come first-served manner. Many questions arise
# with this configuration. The most important of these might be whether the printer is capable of
# handling a certain amount of work. If it cannot, students will be waiting too long for printing
# and may miss their next class.
# Consider the following situation in a computer science laboratory. On any average day about
# 10 students are working in the lab at any given hour. These students typically print up to twice
# during that time, and the length of these tasks ranges from 1 to 20 pages. The printer in the
# lab is older, capable of processing 10 pages per minute of draft quality. The printer could be
# switched to give better quality, but then it would produce only five pages per minute. The
# slower printing speed could make students wait too long. What page rate should be used?

class Printer:
	def __init__(self, ppm):
		"""initializing the printer class"""
		self.page_rate = ppm
		self.current_task = None
		self.time_remaining = 0
	def tick(self):
		"""Counting task remaining time"""
		if self.current_task != None:
			self.time_remaining = self.time_remaining - 1
		if self.time_remaining <= 0:
			self.current_task = None
	def busy(self):
		"""Printer status"""
		if self.current_task != None:
			return True
		else:
			return False

	def start_next(self, new_task):
		"""initializing next task"""
		self.current_task = new_task
		self.time_remaining = (new_task.get_pages() * 60) / self.page_rate