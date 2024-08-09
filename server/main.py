from fastapi import FastAPI, Depends, HTTPException  # noqa: F401
from sqlalchemy.orm import Session
from datetime import datetime
from loguru import logger
from . import models, database, auth
from .database import engine
from pydantic import BaseModel
from config import DATABASE_URL, API_KEYS  # noqa: F401

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

logger.add("server.log", rotation="500 MB")

class LogEntry(BaseModel):
    timestamp: datetime
    service_name: str
    log_level: str
    message: str

@app.post("/logs")
async def create_log(log: LogEntry, db: Session = Depends(database.get_db), api_key: str = Depends(auth.get_api_key)):
    db_log = models.Log(**log.dict(), received_at=datetime.utcnow())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    logger.info(f"Received log: {log}")
    return {"status": "success"}

@app.get("/logs")
async def get_logs(start_date: datetime = None, end_date: datetime = None, db: Session = Depends(database.get_db)):
    query = db.query(models.Log)
    if start_date:
        query = query.filter(models.Log.timestamp >= start_date)
    if end_date:
        query = query.filter(models.Log.timestamp <= end_date)
    logs = query.all()
    return logs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)