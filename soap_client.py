import random

def enviar_certificacion_soap(solicitud):
    # Simulación de llamada SOAP con posible fallo
    estados = ["procesado", "en revisión", "rechazado"]
    return random.choice(estados)
