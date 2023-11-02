from fastapi import FastAPI, status, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from routes import user_routes

app = FastAPI()


@app.get("/status", status_code=status.HTTP_200_OK)
def health_check():

    return JSONResponse(content='Status OK')


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router, prefix="/user", tags=['Usuários'])

# python -m uvicorn app:app --reload