# celery-template

## 启动集群管理端
- docker run --name flower -v ${PWD}/src:/opt -w /opt  -p 5555:5555 mher/flower celery -A tasks flower



## 创建镜像

- docker build -t celery ./docker

## 执行 Celery 命令参考
- docker run -it -v ${PWD}/src:/root -w /root celery bash
- celery -A tasks worker --loglevel=info
- celery -A tasks worker -l info -E

