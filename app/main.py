from celery import Celery
from tasks import Task


app = Celery("tasks", broker='redis://192.168.3.42:6379/0', backend='redis://192.168.3.42:6379/0')




@app.task
def http():
    Task()
    