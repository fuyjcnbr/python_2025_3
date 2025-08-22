
https://python-type-challenges.zeabur.app

docker build --no-cache --squash -t python_hw_3 -f Dockerfile .


docker run -it python_hw_3 /bin/bash

docker run -v ~/PycharmProjects/python_2025_3:/src -it python_hw_3 /bin/bash

make typing

