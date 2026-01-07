

## Примеры с https://python-type-challenges.zeabur.app


## Собираем docker-образ
```commandline
docker build --no-cache --squash -t python_hw_3 -f docker/Dockerfile .
```


## Запускаем docker контейнер
```commandline
docker run -v .:/src -it python_hw_3 /bin/bash
```


## В docker контейнере

### Проверяем аннтотации
```commandline
make typing
```











docker run -v ~/PycharmProjects/python_2025_3:/src -it python_hw_3 /bin/bash



