from sqlalchemy import Column, Integer, String, Text
from database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    phone = Column(String(20), nullable=False)

    email = Column(String(150), nullable=True)

    date = Column(String(50), nullable=False)

    time = Column(String(50), nullable=False)

    message = Column(Text, nullable=True)