#Clase Tiempo

class Time(object):
	
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second
	
	def __str__(self):
		return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)
	
	def print_time(self):
		print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)
	
	def int_to_time(self):
		return self.hour+':'+''+self.minute+':'self.seconds

	def __add__(self, other):
		seconds = self.int_to_time(self.seconds) + self.int_to_time(other.seconds)
		return seconds

	def time_to_int(self):
		tot_h = self.hour * (60 * 60)
		tot_m = self.minute * 60
		return tot_h + tot_m + self.seconds

