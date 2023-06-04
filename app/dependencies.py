from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from crud import get_user_by_token
from models.users import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

engine = create_async_engine(settings.DATABASE_URL, echo=True)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        expire_on_commit=False,
        class_=AsyncSession,
        bind=engine,
    )
    async with async_session() as session:
        yield session


async def get_current_user(
    db: AsyncSession = Depends(get_session),
    token: str = Depends(oauth2_scheme),
) -> User:
    user = await get_user_by_token(db, token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user


DBSession = Annotated[AsyncSession, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]
