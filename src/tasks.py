from celery import Celery


app = Celery("tasks", broker='redis://192.168.3.42:6379/0', backend='redis://192.168.3.42:6379/0')
# app.conf.CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
# app.conf.CELERY_WORKER_SEND_TASK_EVENTS = True




@app.task
def add(x, y):
    return x + y



