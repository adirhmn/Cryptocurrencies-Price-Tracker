from fastapi import FastAPI
from api.api import router as api_router
from database.session import engine, get_db, Base
from utils.exception import CustomHTTPException

# Membuat tabel-tabel di database
Base.metadata.create_all(bind=engine)

# Inisialisasi FastAPI
app = FastAPI()

# Mengimpor rute API dari api_router
app.include_router(api_router)

@app.exception_handler(CustomHTTPException)
async def custom_http_exception_handler(request, exc: CustomHTTPException):
    return exc.as_response()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
