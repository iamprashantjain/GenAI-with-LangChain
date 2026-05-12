from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name:str = 'prashant'
    age:Optional[int] = None
    email:EmailStr
    cgpa:float=Field(gt=0, lt=10, default=5, description="cgpa of student")

new_s = {'age':'5', 'email':'p@p.com', 'cgpa':1}
student = Student(**new_s)
print(student)
