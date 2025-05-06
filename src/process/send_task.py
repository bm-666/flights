from tasks import test

test.apply_async(queue="tasks")