from pydantic import BaseModel, EmailStr


class AppointmentCreate(BaseModel):
    name: str
    phone: str
    email: EmailStr | None = None
    date: str
    time: str
    message: str | None = None