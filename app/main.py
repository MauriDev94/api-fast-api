from fastapi import FastAPI
from app.core.http_errors import register_exception_handler
from app.features.admin.country import v1_admin_country_router

app = FastAPI(
    title="Admin API",
)
app.include_router(v1_admin_country_router, tags=["V1 Admin Country"])
register_exception_handler(app)
