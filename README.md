# Shorter URL

Un acortador de URLs construido con Django que permite a los usuarios crear enlaces cortos y administrarlos de forma sencilla.

## Características

- Creación de URLs cortas con nombres personalizados
- Redirección instantánea a la URL original
- Sistema de autenticación de usuarios
- Panel de administración para gestionar URLs
- Búsqueda de URLs por nombre
- Diseño responsive con Bootstrap
- Soft delete (eliminación lógica) de registros

## Tecnologías

- **Backend:** Django 6.0.6
- **Base de datos:** SQLite (desarrollo) / PostgreSQL (producción)
- **Python:** >=3.14
- **Gestor de paquetes:** uv

## Estructura del proyecto

```
shorter_url/
├── config/                 # Configuración del proyecto Django
│   ├── settings/          # Configuraciones por entorno
│   │   ├── base.py        # Configuración base
│   │   ├── development.py # Configuración de desarrollo
│   │   └── production.py  # Configuración de producción
│   ├── urls.py            # URLs principales
│   └── utils.py           # Utilidades y modelos abstractos
├── shorter/               # Aplicación principal
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas
│   ├── urls.py            # Rutas de la aplicación
│   ├── forms.py           # Formularios
│   └── templates/         # Templates HTML
├── static/                # Archivos estáticos
├── .env.template          # Plantilla de variables de entorno
├── manage.py              # Script de administración de Django
└── pyproject.toml         # Configuración del proyecto Python
```

## Requisitos previos

- Python 3.14 o superior
- uv (gestor de paquetes)
- Git

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd shorter_url
```

2. Crear y activar el entorno virtual:
```bash
uv venv
# En Windows:
.venv\Scripts\activate
# En Linux/Mac:
source .venv/bin/activate
```

3. Instalar las dependencias:
```bash
uv sync
```

4. Configurar las variables de entorno:
```bash
cp .env.template .env
```

5. Editar el archivo `.env` con tus configuraciones:
```env
DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_db
DJANGO_ENV=development
DJANGO_SECRET_KEY=tu_clave_secreta_aqui
```

## Configuración de base de datos

### SQLite (Desarrollo)
La configuración de desarrollo usa SQLite por defecto. No se requiere configuración adicional.

### PostgreSQL (Producción)
1. Instalar PostgreSQL
2. Crear la base de datos
3. Actualizar `DATABASE_URL` en el archivo `.env`

## Uso

1. Ejecutar las migraciones:
```bash
python manage.py migrate
```

2. Crear un superusuario:
```bash
python manage.py createsuperuser
```

3. Ejecutar el servidor de desarrollo:
```bash
python manage.py runserver
```

4. Acceder a la aplicación:
- Página principal: http://localhost:8000/
- Panel de administración: http://localhost:8000/auth/admin/

## Endpoints

| Ruta | Método | Descripción | Autenticación |
|------|--------|-------------|---------------|
| `/` | GET | Página de aterrizaje | No |
| `/login/` | GET/POST | Inicio de sesión | No |
| `/logout/` | GET | Cierre de sesión | Sí |
| `/user/<username>/` | GET | Lista de URLs del usuario | No |
| `/url/create/` | GET/POST | Crear nueva URL corta | Sí |
| `/<username>/<short_url>/` | GET | Redirigir a URL original | No |

## Modelo de datos

### ShortURL
- `original_url`: URL original a redirigir
- `name`: Nombre único de la URL corta
- `user`: Usuario propietario (ForeignKey)
- `created_at`: Fecha de creación
- `updated_at`: Fecha de última actualización
- `deleted_at`: Fecha de eliminación (soft delete)

## Variables de entorno

| Variable | Descripción | Valores permitidos |
|----------|-------------|-------------------|
| `DATABASE_URL` | URL de conexión a la base de datos | URL de PostgreSQL |
| `DJANGO_ENV` | Entorno de ejecución | `development`, `production` |
| `DJANGO_SECRET_KEY` | Clave secreta de Django | Cadena aleatoria segura |

## Desarrollo

### Estructura de configuración
- `config/settings/base.py`: Configuración compartida
- `config/settings/development.py`: Configuración para desarrollo
- `config/settings/production.py`: Configuración para producción

### Modelo AuditModel
Todos los modelos heredan de `AuditModel` que proporciona:
- `created_at`: Marca de tiempo de creación
- `updated_at`: Marca de tiempo de actualización
- `deleted_at`: Soft delete

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo LICENSE para más detalles.
