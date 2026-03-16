from fastapi import FastAPI
from content_factory.api.routes import router

app = FastAPI()
app.include_router(router)
