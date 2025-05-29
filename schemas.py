from pydantic import BaseModel

class SolicitudIn(BaseModel):
    tipo: str
    estudiante_id: int
    datos_adicionales: str

class SolicitudOut(BaseModel):
    id: int
    estado: str
    mensaje: str
