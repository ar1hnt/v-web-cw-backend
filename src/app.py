from fastapi import FastAPI

from src import router


app = FastAPI(
    title="digit.", 
    description="API технологического форума для студентов IT-направлений.", 
    redoc_url=None,
    docs_url="/api/docs",
    )
app.include_router(router)