from db.database import Base
from sqlalchemy import Column, Integer, String, Float

class LoanApplication(Base):
        __tablename__ = 'loan_applications'

        id=Column(Integer, primary_key=True, index=True)
        name=Column(String)
        email=Column(String)
        income=Column(Float)
        loan_amount=Column(Float)
        loan_type=Column(String)
        document_path=Column(String, nullable=True)