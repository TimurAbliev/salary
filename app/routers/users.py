from fastapi import APIRouter, HTTPException, status

from crud import create_user_token, get_user_by_username
from dependencies import CurrentUser, DBSession
from schemas.users import LoginSerializer, TokenSerializer, UserSerializer

router = APIRouter()


@router.get("/", response_model=UserSerializer)
async def me(current_user: CurrentUser):
    return current_user


@router.post("/login/", response_model=TokenSerializer)
async def login(user: LoginSerializer, db: DBSession):
    user_db = await get_user_by_username(db, username=user.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    if user_db.password != user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    user_db.token = await create_user_token(db, user=user_db)
    return user_db.token
