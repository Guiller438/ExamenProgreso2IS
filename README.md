# 🎓 SolicitudService – Microservicio de Solicitudes Académicas

`SolicitudService` es un microservicio desarrollado como parte de la **Plataforma de Servicios Estudiantiles**, orientado a la **integración de sistemas educativos** mediante una arquitectura distribuida basada en microservicios. Permite a los estudiantes registrar y consultar solicitudes académicas (como certificados, homologaciones, entre otros), y se conecta a un sistema externo simulado vía **SOAP**, integrando mecanismos de **seguridad**, **resiliencia** y **documentación interactiva**.

---

## 📌 Endpoints Disponibles

| Método | Ruta                  | Descripción                             |
|--------|-----------------------|-----------------------------------------|
| POST   | `/solicitudes`        | Crea una nueva solicitud académica      |
| GET    | `/solicitudes/{id}`   | Consulta el estado de una solicitud     |

---

## 🧰 Tecnologías Utilizadas

- 🐍 **FastAPI** – Framework ligero y rápido para APIs en Python
- 🔐 **JWT (JSON Web Token)** – Seguridad por autenticación basada en tokens
- 🔄 **Tenacity** – Implementación de políticas de reintento ante fallos SOAP
- ☁️ **Simulación SOAP** – Simulación de servicios externos no REST
- 🧪 **Postman** – Pruebas manuales de endpoints con tokens
- 🌐 **OpenAPI/Swagger** – Documentación de endpoints automáticamente generada
- 🚪 **Ocelot API Gateway (.NET)** – Enrutamiento, seguridad y políticas de acceso
- ⚙️ **Docker** – Contenerización de servicios
- 🧵 **YAML / Istio (Simulado)** – Configuración de resiliencia y circuit breakers

---

## 🔧 Instalación y Ejecución

### ✅ Requisitos

- Python 3.8 o superior
- pip para instalar dependencias
- Git
- (Opcional) Docker

### 🚀 Pasos para instalación local

```bash
git clone https://github.com/tu_usuario/solicitud_service.git
cd solicitud_service
python -m venv venv
.
env\Scripts ctivate  # En Windows
# source venv/bin/activate  # En Linux o Mac
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🔐 Seguridad

Este microservicio utiliza **autenticación JWT** para proteger los endpoints. Para acceder a ellos:

1. Solicita un token JWT desde un sistema de autenticación (simulado o real).
2. Incluye el token en el encabezado `Authorization` con el formato:

```
Authorization: Bearer <tu_token_aquí>
```

---

## 🔄 Resiliencia y Gestión de Errores

Se ha incorporado la librería `tenacity` para aplicar:

- **Reintentos automáticos (retry)** al servicio SOAP con un máximo de **2 intentos**.
- **Circuit Breaker simulado**, integrado en YAML (estilo Istio), que bloquea llamadas tras **3 fallos en 60 segundos**.

Ejemplo conceptual en YAML:

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: solicitudservice
spec:
  http:
    - route:
        - destination:
            host: solicitudservice
      retries:
        attempts: 2
        perTryTimeout: 2s
        retryOn: gateway-error,connect-failure,refused-stream
      fault:
        abort:
          httpStatus: 500
          percentage:
            value: 25.0
```

---

## 🧪 Pruebas con Postman

Se incluye una colección de Postman para facilitar las pruebas:

- Verifica los headers con JWT.
- Simula solicitudes válidas y con error.
- Muestra respuestas esperadas del sistema.

---

## 🔄 Integración con Servicios SOAP (Simulado)

Este microservicio se comunica con un sistema externo **SOAP** que fue **simulado** para pruebas de resiliencia y compatibilidad con sistemas legacy.

- La integración se realiza a través de funciones que emulan respuestas SOAP.
- Se valida la interoperabilidad con servicios no RESTful.

---

## 🛡️ Gateway y Políticas de Seguridad

A través del **API Gateway Ocelot**, se aplican las siguientes políticas:

- 🔑 **Autenticación por JWT** en `/solicitudes`
- ⏳ **Rate limiting** para evitar abusos
- 🧱 **Reintentos y fallbacks** desde el gateway

---

## 📦 Docker (opcional)

Para ejecutar el servicio usando Docker:

```bash
docker build -t solicitudservice .
docker run -d -p 8000:8000 solicitudservice
```

---

## 🗃️ Estructura del Proyecto

```
solicitud_service/
│
├── main.py                   # Entrada principal del microservicio
├── routers/
│   └── solicitud_router.py   # Rutas y lógica del CRUD de solicitudes
├── services/
│   └── soap_service.py       # Simulación de llamadas a sistema SOAP
├── utils/
│   └── auth.py               # Manejo de autenticación JWT
├── schemas/
│   └── solicitud.py          # Validación de datos y modelos Pydantic
├── tests/
│   └── test_solicitudes.py   # Pruebas unitarias (opcional)
├── requirements.txt
└── README.md
```

---

## 📈 Futuras Mejoras

- Conexión real a un backend SOAP empresarial
- Persistencia en base de datos SQL (PostgreSQL, SQL Server)
- Métricas Prometheus + Dashboard Grafana
- CI/CD con Jenkins o GitHub Actions
- Pruebas automatizadas con `pytest`

---

## 👨‍💻 Autor

**Guillermo Álvarez**  
Estudiante de Ingeniería de Software  
Ecuador 🇪🇨 | GitHub: [@Guiller438](https://github.com/Guiller438)

---
