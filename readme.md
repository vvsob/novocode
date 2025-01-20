# Novocode

A testing system created by me in 2023. It relies on a testing library I wrote called `strategy`. It's main concept is to allow problem writers to define the testing procedure of the task with a python file called "strategy". Unfortunately, I never got to fully implementing this idea, but I got a working prototype that is in this repository.

This repository contains the frontend for the testing system. It is written in Python, using Django. The web server also provides a REST API that is used by the invoker. The REST API is implemented using Django REST framework.

For the invoker see https://github.com/vvsob/novocode-invoker/

## Deployment

See https://gist.github.com/vvsob/9bc666bf28be61fa7c0fb003bf70b5b8
