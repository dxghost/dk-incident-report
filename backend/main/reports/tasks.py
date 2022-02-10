import httpx
import json
from reporter.settings import (
    REDIS_DB,
    REDIS_PORT,
    REDIS_HOST,
    REDIS_FETCH_LOGS_COUNTER_KEY,
)
import redis
from reports.models import IncidentReport
from reporter.settings import MONITOR_HOST, MONITOR_PORT

redis_instance = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def fetch_logs():
    redis_counter = redis_instance.get(REDIS_FETCH_LOGS_COUNTER_KEY)
    if redis_counter == None:
        redis_counter = IncidentReport.objects.count()
        redis_instance.set(REDIS_FETCH_LOGS_COUNTER_KEY, redis_counter)
    else:
        redis_counter = int(redis_counter)

    resp = httpx.get(
        "http://{}:{}/logs/?start={}".format(MONITOR_HOST, MONITOR_PORT, redis_counter)
    )
    dt = json.loads(resp.text)
    dt = dt.get("results")

    redis_instance.incr(REDIS_FETCH_LOGS_COUNTER_KEY, len(dt))
    return dt


