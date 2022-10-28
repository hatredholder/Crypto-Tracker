# Crypto-Tracker

:money_with_wings: :money_with_wings: :money_with_wings:

A Crypto Currency Tracker project based on Django 4.0 that is made to track prices on top 100 crypto currences in **realtime** which is achieved by using Django Channels. Data is gathered from the [Coingecko API](https://www.coingecko.com/). 

Scroll down to see the **Instructions** on how to launch this project properly. 

## Preview 

![crypto_proj_1](https://user-images.githubusercontent.com/86254474/172397460-2806f735-013d-4188-9020-47550dac31b1.png)

## Instructions

Clone this repository, cd into it

```
git clone https://github.com/hatredholder/Crypto-Tracker.git
cd Crypto-Tracker
```    

Start a new **Virtualenv**, activate it, install Python module requirements

```
virtualenv myenv
source myenv/bin/activate
pip install -r requirements.txt
```
Run the **Redis** server
```
redis-server
```
Run a **Celery** worker
```
celery -A crypto_proj worker
```
Run the **Celery** beat
```
celery -A crypto_proj beat
```
Finally, run the **Django** server
```
python manage.py runserver
```

## Technologies

Frontend: Basic HTML.

Backend: Django 4.0, Celery, Redis (for Celery message broking and Django Channels layers).

Database: SQLite.

## To Do/To Add

- [x] Update template JavaScript logic;

- [x] Implement Django Channels connection
