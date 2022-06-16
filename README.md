# Crypto-Tracker

:money_with_wings: :money_with_wings: :money_with_wings:

A Crypto Currency Tracker project based on Django 4.0 that is made to track prices on top 100 crypto currences in realtime. Data is gathered from the [Coingecko API](https://www.coingecko.com/). Scroll down to see the **Instructions** on how to launch this project properly. 

## Preview: 

![crypto_proj_1](https://user-images.githubusercontent.com/86254474/172397460-2806f735-013d-4188-9020-47550dac31b1.png)

## Instructions

1. Clone this repository
2. Run a Redis server on port 6379 (this port is set by default) - https://redis.io/docs/getting-started/
3. Run a Celery worker - https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html
4. Run a Celery beat - https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html
5. Run the Django server by typing in console `py manage.py runserver`

## Technologies

Frontend: Basic HTML.

Backend: Django 4.0, Celery, Redis (for Celery message broking and Channels layers).

Database: SQLite.

## To Do/To Add:

- [x] Implement Django Channels connection; 





