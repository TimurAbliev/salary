import uuid

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

from core.utils import default_date

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    salary = Column(Float)
    update_salary = Column(DateTime, default=default_date())

    tokens = relationship(
        "Token",
        back_populates="user",
        lazy="dynamic",
        cascade="all, delete-orphan",
    )


class Token(Base):
    __tablename__ = "users_tokens"

    id = Column(Integer, primary_key=True)
    token = Column(
        UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4
    )
    expires = Column(DateTime)
    user_id = Column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    user = relationship("User", back_populates="tokens", lazy="joined")
