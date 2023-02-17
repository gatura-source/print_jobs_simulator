
from print_jobs import Printer
from task import Task
from dst import Queue
import random

def new_print_task():

	num = random.randint(1, 18)
	if num == 18:
		return True
	else:
		return False


def simulation(num_seconds, pages_per_mins):
	"""Carries the simulation"""
	lab_printer = Printer(pages_per_mins)
	print_queue = Queue()
	waiting_times = []

	for current_second in range(num_seconds):
		# print(f"***Current Second -- {current_second}***")
		if new_print_task():
			task = Task(current_second)
			# print(f"Task Created at {current_second}")
			print_queue.enqueue(task)

		if (not lab_printer.busy()) and (not print_queue.is_empty()):
			next_task = print_queue.dequeue()
			waiting_times.append(next_task.wait_time(current_second))
			# print(f"Wait Time:: --{current_second}")
			lab_printer.start_next(next_task)


		lab_printer.tick()

	average_wait = sum(waiting_times) / len(waiting_times)
	print(f"Average Wait time {average_wait:.2f} -- {print_queue.size()} tasks remaining")
for i in range(10):
	simulation(3600, 10)