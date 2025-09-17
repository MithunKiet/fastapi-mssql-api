from fastapi import FastAPI
from app.routers import health_router, user_router

def create_app() -> FastAPI:
    app = FastAPI(title="MSSQL API", version="1.0.0")
    app.include_router(user_router.router)
    @app.get("/health")
    def health():
        return {"status": "ok"}
    app.include_router(health_router.router)   # 👈 add this line
    return app

app = create_app()
