from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from models.users import Token, User


async def get_user_by_token(db: AsyncSession, token: str) -> User:
    statement = (
        select(Token)
        .where(Token.token == token)
        .options(joinedload(Token.user))
    )
    result = await db.execute(statement)
    token = result.scalars().first()
    return token.user


async def get_user_by_username(db: AsyncSession, username: str) -> User:
    statement = select(User).where(User.username == username)
    result = await db.execute(statement)
    return result.scalars().first()


async def create_user_token(db: AsyncSession, user: User) -> Token:
    db_token = Token(user=user, expires=datetime.now() + timedelta(weeks=1))
    db.add(db_token)
    await db.commit()
    return db_token
