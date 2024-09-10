import uvicorn

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

import crud
import schemas
import models

from database import SessionLocal, engine

# create database tables
models.Base.metadata.create_all(bind=engine) # temporary: to initialize with alembic

app = FastAPI()

"""
This is a Dependency.
We need to have an independent database session/connection (SessionLocal) 
per request, use the same session through all the request and then close 
it after the request is finished
"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/brilliant_thing/", response_model=schemas.BrilliantThing)
async def add_brilliant_thing(brilliant_thing: schemas.BrilliantThingCreate, db: Session = Depends(get_db)):
    new_entry = crud.create_brilliant_thing(db, brilliant_thing=brilliant_thing)
    if new_entry:
        return JSONResponse(content={"message":f"Brilliant Thing #{new_entry.id} added successfully!"}, status_code=201)
    

@app.get("/brilliant_thing/", response_model=schemas.BrilliantThing)
def read_brilliant_thing(db: Session = Depends(get_db)):
    brilliant_thing = crud.get_brilliant_thing(db)
    if brilliant_thing:
        return brilliant_thing
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)