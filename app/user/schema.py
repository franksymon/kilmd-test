from sqlmodel import Field, SQLModel
from pydantic import EmailStr
from app.role.schema import RolePublicSchema
from typing import Optional




class UserBaseSchema(SQLModel):
    id: int
    email: str
    username: str  
    #full_name: str
    #role: Optional[RolePublicSchema]
    #is_active: bool


class GetUserSchema(UserBaseSchema):
    role: Optional[RolePublicSchema]
    is_active: bool

class UserCreateSchema(SQLModel):
    email: EmailStr = Field(max_length=255)
    username: str  
    full_name: str
    password: str = Field(min_length=8, max_length=40)
    role_id:  int 
   

class UpdatePasswordSchema(SQLModel):
    current_password: str = Field(min_length=8, max_length=40)
    new_password: str = Field(min_length=8, max_length=40)


class OperatorSchema(UserBaseSchema):
    ...


class InvestorSchema(UserBaseSchema):
    ...


class TransactionUserSchema(UserBaseSchema):
    ...