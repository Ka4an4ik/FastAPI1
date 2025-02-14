from fastapi import FastAPI
import uvicorn
import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Client as SchemaClient
from schema import History as SchemaHistory
from schema import Link as SchemaLink

from schema import Client
from schema import History
from schema import Link

from models import Link as ModelLink
from models import History as ModelHistory
from models import Client as ModelClient

import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv('.env')


@app.get("/", summary="Приветствие")
async def hello():
    return {"1" : "hello"}



app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.post('/client/', response_model=SchemaClient)
async def client(client: SchemaClient):
    db_client = ModelClient(telegram_id=client.telegram_id, active_till=client.active_till, date_created = client.date_created)
    db.session.add(db_client)
    db.session.commit()
    return db_client

@app.get('/get_clients/')
async def get_clients():
    clients = db.session.query(ModelClient).all()
    return clients



@app.post('/link/', response_model=SchemaLink)
async def link(link:SchemaLink):
    db_link = ModelLink(link=link.link, date_created=link.date_created, date_updated = link.date_updated)
    db.session.add(db_link)
    db.session.commit()
    return db_link

@app.get('/links/')
async def get_links():
    link = db.session.query(ModelLink).all()
    return link



@app.post('/history',response_model=SchemaHistory)
async def history(history:SchemaHistory):
    db_history = ModelHistory(date = history.date, date_created = history.date_created, parent_id = history.parent_id)
    db.session.add(db_history)
    db.session.commit
    return db_history

@app.get('/histories/')
async def get_histories():
    history = db.session.query(ModelHistory).all()
    return history



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)