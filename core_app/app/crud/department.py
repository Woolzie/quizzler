from models import Department, DepartmentCreate
from sqlmodel import Session, select, delete
import uuid

def create_department(*, session: Session, department_info: DepartmentCreate):
    new_department = Department.model_validate(
        department_info,
    )
    
    session.add(new_department)
    session.commit()
    session.refresh(new_department)
    
    return new_department

def get_department(*, session: Session, department_id: uuid):
    department_obj = session.get(Department, department_id)
    
    return department_obj

def delete_department(*, session: Session, department_id: uuid):
    delete_stmnt = delete(Department).where(Department.department_id == department_id)
    session.exec(delete_stmnt)
    session.commit()