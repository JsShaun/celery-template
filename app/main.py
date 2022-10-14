from celery import Celery
import tasks
import trio


app = Celery("tasks", broker='redis://192.168.3.42:6379/0', backend='redis://192.168.3.42:6379/0')




@app.task
def http():
    trio.run(tasks.Task)