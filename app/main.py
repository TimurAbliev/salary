import uvicorn
from fastapi import FastAPI
from sqladmin import Admin

from dependencies import engine
from internal.admin import UserAdmin, authentication_backend
from routers.users import router as users_router

app = FastAPI()

admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.register_model(UserAdmin)

app.include_router(users_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
