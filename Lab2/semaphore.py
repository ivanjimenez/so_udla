class RLock:
	def __init__(self):
		self._block = _allocate_lock()
		self._owner = None
		self._count = 0

	def acquire(self, blocking=1):
		me = current_thread()
		if self._owner is me:
			self._count = self._count + 1
			return 1
			
		rc = self._block.acquire(blocking)
		if rc:
			self._owner = me
			self._count = 1
		return rc
		
	def release(self):
		if self._owner is not current_thread():
			raise RuntimeError("cannot realease an un-acquired lock")
		self._count = count = self._count - 1
		if not count:
			self._owner = None
			self._block.release()