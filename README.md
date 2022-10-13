# celery-template


## 启动集群管理端
- docker run --name flower -v ${PWD}/app:/root -w /root  -p 5555:5555 mher/flower celery -A tasks flower


## 创建镜像

- docker build -t celery ./docker

## Celery集群 
- docker run -it -v ${PWD}/app:/root -w /root celery bash
- celery -A tasks worker --loglevel=info
- celery -A tasks worker -l info -E

