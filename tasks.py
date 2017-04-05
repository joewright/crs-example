from celery import Celery
from celery_redis_sentinel.task import EnsuredRedisTask
from celery_redis_sentinel import register as register_sentinel_backend


BROKER_TRANSPORT_OPTIONS = {
    'sentinels': [('redis-sentinel-cluster', 26379),
                  ('redis-sentinel-cluster', 26380),
                  ('redis-sentinel-cluster', 26381)],
    'service_name': 'redis_dev_master',
    'socket_timeout': 0.1
}

# has to be called before creating celery app
register_sentinel_backend()

app = Celery('tasks')
app.conf.update(BROKER_URL='redis-sentinel://redis-sentinel-cluster:26379/0',
                BROKER_TRANSPORT_OPTIONS=BROKER_TRANSPORT_OPTIONS,
                CELERY_ACCEPT_CONTENT=['json'],
                CELERY_RESULT_BACKEND='redis-sentinel://redis-sentinel-cluster:26379/1',
                CELERY_RESULT_BACKEND_TRANSPORT_OPTIONS=BROKER_TRANSPORT_OPTIONS,
                CELERY_TASK_SERIALIZER='json',
                CELERY_RESULT_SERIALIZER='json')


@app.task(base=EnsuredRedisTask)
def my_cool_task(data):
    print(data)
