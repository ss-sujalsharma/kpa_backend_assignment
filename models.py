# In models.py

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import JSON
from database import Base # <--- CORRECTED IMPORT

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, index=True)
    submittedBy = Column(String, index=True)
    submittedDate = Column(Date)
    fields = Column(JSON)
