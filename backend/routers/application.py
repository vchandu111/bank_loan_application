from fastapi import APIRouter, Form, UploadFile, File, Depends
from sqlalchemy.orm import Session
from db.database import get_db
import os
from db.models import LoanApplication

router = APIRouter(
        prefix="/api",
        tags=["Application"]
)

@router.post("/apply")
async def applyForLoan(
        name:str = Form(...),
        email:str = Form(...),
        income:float = Form(...),
        loan_amount:float = Form(...),
        loan_type:str = Form(...),
        file:  UploadFile = File(...),
        db: Session = Depends(get_db)
        ):

        os.makedirs("uploads", exist_ok=True)
        file_path = f'uploads/{file.filename}'

        new_application = LoanApplication(
                name=name,
                email=email,
                income=income,
                loan_amount=loan_amount,
                loan_type=loan_type,
                document_path=file_path
        )

        db.add(new_application)
        db.commit()
        db.refresh(new_application)

        return {"id": new_application.id, "message":"Application submitted successfully."}

@router.get("/applications/all")
def get_all_applications(db:Session=Depends(get_db)):
        applications = db.query(LoanApplication)
        return {"applications":applications}

@router.get("/applications/{id}")
def get_applications(id: int, db:Session = Depends(get_db)):
        
        return db.query(LoanApplication).filter(LoanApplication.id == id).first()