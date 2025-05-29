from fastapi import FastAPI, Depends
from schemas import SolicitudIn, SolicitudOut
from auth import validar_token
from soap_client import enviar_certificacion_soap

app = FastAPI()

solicitudes_db = {}  # Simulación de base de datos
counter = 1

@app.post("/solicitudes", response_model=SolicitudOut)
def crear_solicitud(solicitud: SolicitudIn, token: str = Depends(validar_token)):
    global counter
    estado = enviar_certificacion_soap(solicitud)
    resultado = {"id": counter, "estado": estado, "mensaje": f"Solicitud registrada con estado: {estado}"}
    solicitudes_db[counter] = resultado
    counter += 1
    return resultado

@app.get("/solicitudes/{id}", response_model=SolicitudOut)
def obtener_solicitud(id: int, token: str = Depends(validar_token)):
    if id not in solicitudes_db:
        return {"id": id, "estado": "desconocido", "mensaje": "Solicitud no encontrada"}
    return solicitudes_db[id]
