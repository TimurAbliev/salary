from typing import Optional

from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from sqladmin import ModelAdmin
from sqladmin.authentication import AuthenticationBackend

from models.users import User


class UserAdmin(ModelAdmin, model=User):
    column_list = [
        User.id,
        User.username,
        User.password,
        User.salary,
        User.update_salary,
    ]
    form_excluded_columns = [User.tokens,]


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        request.session.update({"token": "..."})
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> Optional[RedirectResponse]:
        if not "token" in request.session:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)


authentication_backend = AdminAuth(secret_key="...")
