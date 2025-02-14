from pydantic import BaseModel
import datetime

class Client(BaseModel):
    id: int 
    telegram_id: int
    active_till: datetime
    date_created: datetime

    class Config:
        orm_mode = True

class Link(BaseModel):
    id: int
    link: str
    date_created: datetime
    date_updated: datetime

    client_id: int

    class Config:
        orm_mode = True
        

class History(BaseModel):
    id: int
    data: str
    date_created: datetime
    parent_id: int

    link_id: int

    class Config:
        orm_mode = True
        