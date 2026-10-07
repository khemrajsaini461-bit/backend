from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Appointment
from schemas import AppointmentCreate


# Database tables create
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Dr. Hemraj Saini API",
    description="Backend API for Dr. Hemraj Saini Website",
    version="1.0.0"
)


# React frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Home API
@app.get("/")
def home():
    return {
        "success": True,
        "message": "Dr. Hemraj Saini Backend is Running",
        "status": "Online"
    }


# Health check
@app.get("/health")
def health_check():
    return {
        "success": True,
        "status": "healthy",
        "message": "API is working correctly"
    }


# Create appointment
@app.post("/appointments")
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):

    new_appointment = Appointment(
        name=appointment.name,
        phone=appointment.phone,
        email=appointment.email,
        date=appointment.date,
        time=appointment.time,
        message=appointment.message
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return {
        "success": True,
        "message": "Appointment booked successfully",
        "appointment_id": new_appointment.id
    }


# Get all appointments
@app.get("/appointments")
def get_appointments(db: Session = Depends(get_db)):

    appointments = db.query(Appointment).all()

    return {
        "success": True,
        "appointments": appointments
    }