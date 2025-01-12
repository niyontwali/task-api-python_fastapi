from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Generic, TypeVar
from pydantic import BaseModel
from app import models, schemas
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task API")

# Define generic type for response model
T = TypeVar('T')

class ResponseModel(BaseModel, Generic[T]):
    ok: bool
    message: str
    data: T
    
    class Config:
        from_attributes = True

@app.post("/tasks/", response_model=ResponseModel[schemas.Task])
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return {"ok": True, "message": "task created successfully", "data": db_task}

@app.get("/tasks/", response_model=ResponseModel[List[schemas.Task]])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).offset(skip).limit(limit).all()
    return {"ok": True, "message": "tasks retrieved successfully", "data": tasks}

@app.get("/tasks/{task_id}", response_model=ResponseModel[schemas.Task])
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True, "message": "task retrieved successfully", "data": task}

@app.put("/tasks/{task_id}", response_model=ResponseModel[schemas.Task])
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    for key, value in task_update.model_dump(exclude_unset=True).items():
        setattr(db_task, key, value)
    
    db.commit()
    db.refresh(db_task)
    return {"ok": True, "message": "task updated successfully", "data": db_task}

@app.delete("/tasks/{task_id}", response_model=ResponseModel[dict])
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(db_task)
    db.commit()
    return {
        "ok": True,
        "message": "task deleted successfully",
        "data": {"id": task_id}
    }