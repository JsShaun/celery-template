# celery-template

## 创建镜像
- docker build -t celery ./docker

## 启动集群管理端
- docker run --name flower -it -v ${PWD}/app:/root -w /root  -p 5555:5555 -p 8888:8888 celery bash
- celery -A process flower --inspect=True --persistent=True

## Celery集群 
- docker run -it -v ${PWD}/app:/root -w /root celery bash
- celery -A process worker --loglevel=info
- celery -A process worker -l info -E
- python test.py


## 启动web
- python web.py