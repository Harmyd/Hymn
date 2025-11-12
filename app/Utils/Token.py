from jose import jwt,JWTError
from typing import Optional
from datetime import timedelta,datetime

def create_access_token(data:dict,expiry:Optional[timedelta]=None):
    to_encode=data.copy()
    if(expiry):
        expiry_date=datetime.utcnow() + expiry
    else:
        expiry_date=datetime.utcnow() + timedelta(hours=1)
    to_encode.update({"exp":expiry_date})
    jwt.encode(to_encode,)


    