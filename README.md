# Crypto-Tracker

:money_with_wings: :money_with_wings: :money_with_wings:

A Crypto Currency Tracker project based on Django 4.0 that is made to track prices on top 100 crypto currences in **realtime**. Data is gathered from the [Coingecko API](https://www.coingecko.com/). 

Scroll down to see the **Instructions** on how to launch this project properly. 

## Preview 

![crypto_proj_1](https://user-images.githubusercontent.com/86254474/172397460-2806f735-013d-4188-9020-47550dac31b1.png)

## Instructions

1. Clone this repository
2. Start a new Virtualenv, activate it, type in console `pip install -r requirements.txt`
3. Run a Redis Server on port 6379 (this port is set by default) - `redis-server`
4. Run the Django Server - `py manage.py runserver`
5. Run a Celery Worker - `celery -A crypto_proj beat`
6. Run a Celery Beat - `celery -A crypto_proj worker`

## Technologies

Frontend: Basic HTML.

Backend: Django 4.0, Celery, Redis (for Celery message broking and Channels layers).

Database: SQLite.

## To Do/To Add

- [x] Implement Django Channels connection
