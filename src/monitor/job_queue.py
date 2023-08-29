from queue import Queue


class JobQueue:

    def __init__(self):
        self.q = Queue(maxsize=1000)

    @property
    def queue(self):
        return self.q

jobQueue = JobQueue()
