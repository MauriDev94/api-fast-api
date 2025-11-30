from fastapi import FastAPI
from app.features.admin.country import v1_admin_country_router

app = FastAPI(
    title="Admin API",
)
app.include_router(v1_admin_country_router, tags=["V1 Admin Country"])
