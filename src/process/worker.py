import asyncio
from redis.asyncio import Redis
from config.settings import config
import redis
from typing import Any
client = redis.from_url(url=config.get_redis_connect_url())
queue = "tasks"

class QueueDoesNot(Exception):
    msg = "QueueDoesNot"

def prt(task: Any) -> None:
    print(f"Task ->{task}")

def run_worker():
    try:
        if client.get(queue) is None:
            raise QueueDoesNot
        while True:
            tasks = client.lrange(queue, 0, -1)
            for task in tasks:
                prt(task)
    except QueueDoesNot as e:
        print(f"Ошибка получения очереди: {e.__class__} - {e.args}")
        raise
    except Exception as e:
        print(f"Неизвестная ошибка: {e.__class__} - {e.args}")





