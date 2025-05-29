from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from schemas import SolicitudIn, SolicitudOut
from auth import validar_token
from soap_client import enviar_certificacion_soap

app = FastAPI()

# Middleware opcional (útil si conectas desde frontend o Postman web)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulación de base de datos
solicitudes_db = {}
counter = 1

# Sistema de autenticación Bearer (para Swagger)
security = HTTPBearer()

@app.post("/solicitudes", response_model=SolicitudOut)
def crear_solicitud(
    solicitud: SolicitudIn,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = validar_token(credentials)  # Validar el JWT
    global counter
    estado = enviar_certificacion_soap(solicitud)
    resultado = {
        "id": counter,
        "estado": estado,
        "mensaje": f"Solicitud registrada con estado: {estado}"
    }
    solicitudes_db[counter] = resultado
    counter += 1
    return resultado

@app.get("/solicitudes/{id}", response_model=SolicitudOut)
def obtener_solicitud(
    id: int,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = validar_token(credentials)  # Validar el JWT
    if id not in solicitudes_db:
        return {
            "id": id,
            "estado": "desconocido",
            "mensaje": "Solicitud no encontrada"
        }
    return solicitudes_db[id]
