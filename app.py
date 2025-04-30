from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata
app = FastAPI(
  title="REST API WITH FastAPI and MongoDB",
  description="This is a simple REST API using Fastapi and mongoDB conection ",
  version="0.0.1",
  openapi_tags=tags_metadata
)


app.include_router(user)
