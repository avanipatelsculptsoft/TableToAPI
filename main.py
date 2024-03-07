from fastapi import FastAPI
from routers import farmInspection, farmers, harvesting, fermatation, strippingData, chemistryLogs
from db import engine
import uvicorn
import models
app = FastAPI()


models.Base.metadata.create_all(bind=engine)
app.include_router(farmers.router)
app.include_router(farmInspection.router)
app.include_router(harvesting.router)
app.include_router(fermatation.router)
app.include_router(strippingData.router)
app.include_router(chemistryLogs.router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)