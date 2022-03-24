from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, relation

from database import Base



class User(Base):
   __tablename__ = "users"

   id = Column(Integer, primary_key=True, index=True)
   authorId = Column(String, unique=True, index=True)
   comments = relationship("Comment", back_populates="author")
