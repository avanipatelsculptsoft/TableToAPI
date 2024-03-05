from fastapi import FastAPI
from routers import customer, contact

app = FastAPI()
app.include_router(customer.router)
app.include_router(contact.router)