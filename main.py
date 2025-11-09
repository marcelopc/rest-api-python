from fastapi import FastAPI
app = FastAPI()
from routes.authRoutes import authRouter
from routes.orderRoutes import orderRouter

app.include_router(authRouter)
app.include_router(orderRouter)