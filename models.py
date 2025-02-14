from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, SMALLINT, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Client(Base):
    __tablename__ = 'client'
    
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(SMALLINT)
    active_till = Column(DateTime(timezone=True))
    date_created = Column(DateTime(timezone=True))

    links = relationship("Link", back_populates="client", cascade="all, delete-orphan")


class Link(Base):
    __tablename__ = 'link'
    
    id = Column(Integer, primary_key=True, index=True)
    link = Column(String)
    date_created = Column(DateTime(timezone=True))
    date_updated = Column(DateTime(timezone=True))

    client_id = Column(Integer, ForeignKey("client.id", ondelete="CASCADE"), nullable=False)
    client = relationship("Client", back_populates="links")


    history = relationship("History", back_populates="link", uselist=False, cascade="all, delete-orphan")


class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String)
    date_created = Column(DateTime(timezone=True))
    parent_id = Column(Integer)


    link_id = Column(Integer, ForeignKey("link.id", ondelete="CASCADE"), nullable=False, unique=True)


    link = relationship("Link", back_populates="history")


