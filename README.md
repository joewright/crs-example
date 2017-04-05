# Celery / Redis Sentinel Example

This is an example of using the [Redis Sentinel Backend](https://github.com/dealertrack/celery-redis-sentinel) to back [Celery](http://www.celeryproject.org/)

It's only been tested with the versions in [requirements.txt](requirements.txt).

The example uses 3 containers

- [Redis Sentinel Cluster](https://github.com/yesuagg/redis-sentinel-cluster)
- Celery container to run the celery task
- Python container to call the celery tasks

### Run it

Clone this repo, load the git submodule, and run the containers
```
git submodule init
git submodule update
docker-compose up
```

You'll see some output from the containers
```
python_1 | calling the task
celery_1 | [2017-04-05 15:34:51,926: WARNING/Worker-2] {"it_worked": true}
```