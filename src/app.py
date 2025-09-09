from fastapi import FastAPI

from src import router


app = FastAPI(
    title="digit.", 
    description="API технологического форума.", 
    redoc_url=None,
    docs_url="/api/docs",
    )
app.include_router(router)