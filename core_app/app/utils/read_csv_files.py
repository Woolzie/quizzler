from crud import student, faculty
from models import User, UserCreate,roles
import csv
import io

def read_users_from_csv(csv_file):
    csv_data =  csv_file.read()
    reader = csv.DictReader(io.StringIO(csv_data))
    return [row for row in reader]
    
def get_students_from_csv(csv_file):
    student_list = read_users_from_csv(csv_file)
    return [student.create_student_model(UserCreate(**new_student)) for new_student in student_list]
    
def get_faculties_from_csv(csv_file):
    faculty_list = read_users_from_csv(csv_file)
    return [faculty.create_faculty_model(UserCreate(**new_faculty)) for new_faculty in faculty_list]