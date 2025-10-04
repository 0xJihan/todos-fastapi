from typing import Annotated

from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database.db import get_db
from models.models import User
from utils.Utils import decodeToken

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")



def authenticate_user(
        token : str = Depends(oauth2_schema),
        db:Session = Depends(get_db)
)->dict:
    payload = decodeToken(token)
    user_id = payload.get("user_id")

    user = db.get(User,user_id)
    if user is None :
        raise HTTPException(status_code=404, detail="Unauthorized access")



    return payload



def require_role(*roles: str):
    def role_dependency(user: dict = Depends(authenticate_user)):

        if user.get("role") not in roles:
            raise HTTPException(status_code=403, detail="Forbidden: insufficient role")
        return user
    return role_dependency


user_dependency = Annotated[dict,Depends(authenticate_user)]