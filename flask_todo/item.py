
import datetime

class Item(object):

    def __init__(self, task, datetime_created=datetime.datetime.now, is_task_complete=False):
        self.task = task
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.is_task_complete = is_task_complete
