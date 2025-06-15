# LIA-UserManagement-GUS
This is the Lia's User Management repository for the "GUS" Service.

---
Genial, Facu. Acá te dejo un `README.md` completo y bien documentado para tu proyecto **UserManagement**, ideal tanto para desarrolladores como para presentar el microservicio:

---

```markdown
# 🧩 UserManagement - LIA Microservice

Microservicio de gestión de usuarios y suscripciones para la plataforma **LIA**. Implementado en Django 5.1.1 y Django REST Framework, expone endpoints RESTful para autenticación, gestión de usuarios y control de consumo de créditos en suscripciones.

---

## 🚀 Características principales

- Autenticación mediante JWT (`djangorestframework_simplejwt`)
- Modelo de usuario customizado (`CustomUser`)
- API REST para usuarios y suscripciones
- Actualización de créditos consumidos con desglose por categoría
- Documentación OpenAPI/Swagger integrada (`drf-spectacular`)
- Conexión a base de datos PostgreSQL, MySQL o SQLite vía `.env`
- CORS y CSRF configurables vía variables de entorno
- Deploy-ready para Railway, Render, etc.

---

## 🛠️ Tecnologías usadas

- Django 5.1.1
- Django REST Framework
- drf-spectacular
- JWT (Simple JWT)
- PyMySQL / psycopg2-binary
- WhiteNoise (servir archivos estáticos)
- Docker y Railway

---

## ⚙️ Configuración del entorno

Crear un archivo `.env` en la raíz con las siguientes variables:

```env
# Django
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,web-production-xxxx.up.railway.app
CSRF_TRUSTED_ORIGINS=https://web-production-xxxx.up.railway.app

# Base de datos
USE_AZURE_POSTGRESQL_DB=False
USE_AZURE_MYSQL_DB=True

# MySQL (si aplica)
MYSQL_DB=user_db
MYSQL_USER=admin
MYSQL_PASSWORD=secret
MYSQL_HOST=mysql-db-host
MYSQL_PORT=3306

# PostgreSQL (si aplica)
AZURE_DB_NAME=
AZURE_DB_USER=
AZURE_DB_PASSWORD=
AZURE_DB_HOST=
AZURE_DB_PORT=5432

# JWT Custom serializer (opcional)
TOKEN_OBTAIN_SERIALIZER=core.serializers.MyTokenObtainPairSerializer
```

---

## 📦 Instalación

```bash
# 1. Clonar el proyecto
git clone https://github.com/tu-usuario/LIA-UserManagement-GUS.git
cd LIA-UserManagement-GUS

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Migraciones
python manage.py migrate

# 5. Crear superusuario (opcional)
python manage.py createsuperuser

# 6. Ejecutar el servidor
python manage.py runserver
```

---

## 🧪 Endpoints principales

| Método | URL                                  | Descripción |
|--------|--------------------------------------|-------------|
| `POST` | `/api/PoC/token/`                    | Obtener token JWT |
| `POST` | `/api/PoC/token/refresh/`            | Refrescar token |
| `POST` | `/api/PoC/token/verify/`            | Verificar token JWT |
| `GET`  | `/api/PoC/user/me/`                  | Obtener datos del usuario autenticado |
| `GET`  | `/api/PoC/subscriptions/`            | Listar suscripciones activas |
| `PUT`  | `/api/PoC/user-subscription/set-credits/` | Actualizar créditos usados |

---

## 🧾 Documentación de la API

Disponible automáticamente al levantar el servidor:

- Swagger UI: `/api/PoC/docs/`
- Redoc: `/api/PoC/redoc/`
- OpenAPI JSON: `/api/PoC/schema/`

---

## 🐳 Docker (opcional)

```bash
# Construir imagen
docker build -t usermanagement .

# Ejecutar contenedor
docker run -p 8000:8000 --env-file .env usermanagement
```

---

## 🧑‍💻 Estructura del proyecto

```
LIA-UserManagement-GUS/
├── manage.py
├── UserManagement/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── core/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── requirements.txt
├── Dockerfile
└── Procfile
```

---

## 📌 Notas

- Usa `PyMySQL` para simplificar el deploy sin dependencias nativas en Railway.
- La autenticación se realiza mediante JWT, por lo tanto las cookies no son necesarias para sesiones.
- El endpoint `/user-subscription/set-credits/` permite sumar créditos usados categorizados (`credits_consumed_detail`)

---
