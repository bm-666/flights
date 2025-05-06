from celery import Celery
from config.settings import config

app = Celery('tasks', broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/0")


@app.task
def test() -> str:
    return "Hello"