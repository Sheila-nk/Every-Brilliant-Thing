import uvicorn

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from . import crud
from . import schemas

from .database import init_db


app = FastAPI(title="Every-Brilliant-Thing")
init_db(app)


@app.post("/brilliant_thing", response_model=schemas.BrilliantThing)
async def add_brilliant_thing(brilliant_thing: schemas.BrilliantThingCreate):
    new_entry = await crud.create_brilliant_thing(brilliant_thing)
    if new_entry:
        return JSONResponse(content={"message":f"Brilliant Thing #{new_entry.id} added successfully!"}, status_code=201)
    raise HTTPException(status_code=400, detail="Failed to add Brilliant Thing. Please try again.")

@app.get("/brilliant_thing", response_model=schemas.BrilliantThing)
async def read_brilliant_thing():
    brilliant_thing = await crud.get_brilliant_thing()
    if brilliant_thing:
        return brilliant_thing
    raise HTTPException(status_code=404, detail="No Brilliant Things yet.")
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)