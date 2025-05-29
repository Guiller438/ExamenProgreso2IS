from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type, CircuitBreaker
import random

class ErrorSOAP(Exception):
    pass

# Creamos un "circuito" con 3 intentos fallidos antes de abrirlo
breaker = CircuitBreaker(
    fail_max=3,
    reset_timeout=30  # 30 segundos antes de cerrar el circuito
)

@retry(
    retry=retry_if_exception_type(ErrorSOAP),
    stop=stop_after_attempt(3),            # máximo 3 intentos
    wait=wait_fixed(2)                     # espera fija de 2 segundos entre intentos
)
@breaker
def enviar_certificacion_soap(solicitud):
    """
    Simula una llamada a un servicio SOAP que puede fallar aleatoriamente.
    """
    if random.choice([True, False, False]):  # 33% chance de fallo
        raise ErrorSOAP("Error al contactar el servicio SOAP")
    
    return random.choice(["procesado", "en revisión", "rechazado"])
