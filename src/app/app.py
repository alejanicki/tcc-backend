from fastapi import FastAPI, status, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from routes import user_routes, battery_routes, deposit_routes, prize_routes, trade_routes, jwt_routes

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
app.include_router(battery_routes.router, prefix="/battery", tags=['Baterias'])
app.include_router(deposit_routes.router, prefix="/deposit", tags=['Deposit'])
app.include_router(trade_routes.router, prefix="/trade", tags=['Trade'])
app.include_router(prize_routes.router, prefix="/prize", tags=['Prize'])
app.include_router(jwt_routes.router, prefix="/auth", tags=['auth'])

# python -m uvicorn app:app --reload