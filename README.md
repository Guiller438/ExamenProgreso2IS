# 🎓 SolicitudService – Microservicio de Solicitudes Académicas

Este microservicio forma parte de la **Plataforma de Servicios Estudiantiles** para la integración de sistemas. Permite a los estudiantes **registrar y consultar solicitudes académicas** (como certificados, homologaciones, etc.) mediante una API REST protegida con tokens JWT y con integración a un sistema externo SOAP simulado.

---

## 📌 Endpoints Disponibles

| Método | Ruta                  | Descripción                              |
|--------|-----------------------|------------------------------------------|
| POST   | `/solicitudes`        | Crea una nueva solicitud académica       |
| GET    | `/solicitudes/{id}`   | Obtiene el estado de una solicitud       |

---

## 🚀 Instalación y Ejecución

### ✅ Requisitos
- Python 3.8 o superior
- `pip` para instalar dependencias

### 🔧 Instalación

```bash
git clone https://github.com/tu_usuario/solicitud_service.git
cd solicitud_service
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
