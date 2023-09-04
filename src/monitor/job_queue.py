from queue import Queue


class JobQueue:

    def __init__(self, maxsize = 1000):
        self.q = Queue(maxsize=maxsize)

    @property
    def queue(self):
        return self.q


jobQueue = JobQueue(maxsize = 1000)

logQueue = JobQueue(maxsize = 10000)
