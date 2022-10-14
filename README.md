# celery-template

## 创建镜像
- docker build -t celery ./docker

## 启动集群管理端
- docker run --name flower -it -v ${PWD}/app:/root -w /root  -p 5555:5555 celery bash
- celery -A main flower

## Celery集群 
- docker run -it -v ${PWD}/app:/root -w /root celery bash
- celery -A main worker --loglevel=info
- celery -A main worker -l info -E
- python process.py

