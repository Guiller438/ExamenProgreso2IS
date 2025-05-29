from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
import jwt

CLAVE_SECRETA = "GuillermoAlvarezIS"


payload = {
    "usuario": "GuillermoAlvarez",
    "rol": "usuario"
}

clave = "GuillermoAlvarezIS"

token = jwt.encode(payload, clave, algorithm="HS256")
print(token)

def validar_token(credentials: HTTPAuthorizationCredentials):
    token = credentials.credentials  # Extrae el token desde el esquema Bearer

    try:
        payload = jwt.decode(token, CLAVE_SECRETA, algorithms=["HS256"])
        return payload  # Puedes retornar información útil como usuario/rol
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token inválido")
