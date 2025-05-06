from fastapi import FastAPI
import uvicorn
from config.settings import config
from api.router import routers


app = FastAPI(root_path="/api/v1")
for router in routers:
    app.include_router(router)



if __name__ == "__main__":
    print(config.get_redis_connect_url())
    uvicorn.run("main:app", reload=True)