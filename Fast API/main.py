from fastapi import FastAPI, HTTPException, Depends,Query
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

Base = declarative_base()
app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)

# Create the tasks table after engine initialization
# Base.metadata.create_all(bind=engine)

class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/tasks/", response_model=list[TaskResponse], summary="View tasks with completion status filter")
def get_tasks(
    
    completed: bool = Query(None, description="Task completion status (true/false)"),
    db: Session = Depends(get_db)
):
    query = db.query(Task)

    # Apply filters based on user input
    if completed is not None:
        query = query.filter(Task.completed == completed) # completed = true/false

    tasks = query.all()
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskResponse, summary="View task by ID")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found")
@app.post("/tasks/", response_model=TaskResponse, summary="Create a new task")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.put("/tasks/{task_id}", response_model=TaskResponse, summary="Update task by ID")
def update_task(task_id: int, updated_task: TaskCreate, db: Session = Depends(get_db)):
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if existing_task:
        for field, value in updated_task.dict().items():
            setattr(existing_task, field, value)
        db.commit()
        db.refresh(existing_task)
        return existing_task
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", summary="Delete task by ID")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return {"message": "Task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")
