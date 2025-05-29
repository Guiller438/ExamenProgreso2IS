from fastapi import HTTPException, Header

def validar_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido")
    
    token = authorization.split(" ")[1]
    
    # Aquí deberías validar el token con el servicio de seguridad
    if token != "tokenvalido123":  # Simulación de validación
        raise HTTPException(status_code=403, detail="Token no autorizado")
        
    return token
