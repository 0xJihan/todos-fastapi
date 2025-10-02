import datetime
from datetime import timedelta, datetime, timezone

import jwt
from pwdlib import PasswordHash

encryptor = PasswordHash.recommended()
SECRET_KEY = "f7d89e6f39a4ab882b211ca9ba302bc6afbd0078a78da809c282a3690b8ef0f1"

def encrypt_password(password: str) -> str:
    return encryptor.hash(password)

def  verify_password(password: str, hashed: str) -> bool:
    return encryptor.verify(password, hashed)


def generateToken(values:dict,delta:timedelta | None = None):

    payload = values.copy()

    date = datetime.now(timezone.utc) + (delta if delta else timedelta(days=7))

    payload.update({
        'exp':date
    })

    return  jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )


def decodeToken(token:str):
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
