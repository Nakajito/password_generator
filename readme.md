git clone https://github.com/Nakajito/password_generator.git
# Generador de Contraseñas Seguras

Proyecto simple en Python + Reflex que genera contraseñas seguras a partir de una longitud indicada por el usuario.

Contenido
- `password_generator/` - Código de la app (componentes Reflex).
- `requirements.txt` - Dependencias del proyecto.

Características
- Genera contraseñas aleatorias (letras, dígitos y símbolos).
- Longitud mínima recomendada: 8 caracteres.
- Validaciones de entrada y mensajes de error en la UI.

Requisitos
- Python 3.12
- (Opcional) Virtualenv/venv

Instalación rápida
1. Clona el repositorio:

```bash
git clone https://github.com/Nakajito/password_generator.git
cd password_generator
```

2. Crea y activa un entorno virtual (recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la app (desarrollo)

Esta aplicación está construida con Reflex. Para iniciar el servidor de desarrollo (según configuración local):

```bash
source .venv/bin/activate
reflex run
```

Abre el navegador en la URL que imprima Reflex (por defecto suele ser `http://localhost:3000`).

Notas sobre la estructura
- `password_generator/components/` contiene los componentes UI (title, description, generator box).
- `password_generator/layout/` contiene el footer y layout relacionados.
- `password_generator/utils.py` incluye la función `generate_password(length)` que se puede probar de forma independiente.


Contribuciones
- Si quieres contribuir, crea una rama nueva, haz tus cambios y abre un pull request.

Licencia
- MIT

---