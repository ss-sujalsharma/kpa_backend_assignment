# In main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware # Import CORS

# This command creates all the database tables defined in models.py
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- Add this new section for CORS ---
# This allows your frontend (running in a browser) to communicate with your backend.
origins = [
    "*" # Allows all origins for simplicity in this assignment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)
# --- End of new section ---


# Dependency to get a DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/forms/wheel-specifications", response_model=schemas.WheelSpecResponse, status_code=201)
def create_wheel_specification(spec: schemas.WheelSpecCreate, db: Session = Depends(get_db)):
    db_spec = db.query(models.WheelSpecification).filter(models.WheelSpecification.formNumber == spec.formNumber).first()
    if db_spec:
        raise HTTPException(status_code=400, detail="Form number already exists")

    new_spec = models.WheelSpecification(
        formNumber=spec.formNumber,
        submittedBy=spec.submittedBy,
        submittedDate=spec.submittedDate,
        fields=spec.fields.dict()
    )
    
    db.add(new_spec)
    db.commit()
    db.refresh(new_spec)

    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": new_spec.formNumber,
            "submittedBy": new_spec.submittedBy,
            "submittedDate": new_spec.submittedDate.isoformat(),
            "status": "Saved"
        }
    }

@app.get("/api/forms/wheel-specifications", status_code=200)
def get_wheel_specifications(db: Session = Depends(get_db)):
    all_specs = db.query(models.WheelSpecification).all()
    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": all_specs
    }

# This is a dummy login endpoint to satisfy the frontend's initial check
@app.post("/api/users/login/")
def dummy_login():
    return {"message": "Dummy login successful"}