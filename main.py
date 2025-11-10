from fastapi import FastAPI
from routes.authRoutes import authRouter
from routes.orderRoutes import orderRouter
from routes.userRoutes import userRouter

app = FastAPI()
app.include_router(authRouter)
app.include_router(orderRouter)
app.include_router(userRouter)