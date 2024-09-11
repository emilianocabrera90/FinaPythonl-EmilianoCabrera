# Mi Blog en Django

Este proyecto es un blog simple creado con Django y Bootstrap. Permite a los usuarios registrarse, iniciar sesión, crear y gestionar posts.

Proyecto realizado unicamente por Emiliano Cabrera

## Estructura del Proyecto

- **Blog**: Manejo de posts del blog.
- **Accounts**: Registro, inicio de sesión y gestión de perfiles de usuario.
- **Templates**: Plantillas HTML que utilizan Bootstrap para el diseño.

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/emilianocabrera90/FinaPythonl-EmilianoCabrera
   cd mi_blog
   ```

2. **Crea un entorno virtual**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

3. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos**:

   ```bash
   python manage.py migrate
   ```

5. **Crea un superusuario**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecuta el servidor de desarrollo**:

   ```bash
   python manage.py runserver
   ```

7. **Accede a la aplicación**:
   - Visita `http://127.0.0.1:8000/` para ver la aplicación en tu navegador.
   - Accede al panel de administración en `http://127.0.0.1:8000/admin/`.

## Uso

- **Home**: Página principal del blog.
- **Crear Post**: Formularios para crear nuevos posts.
- **Editar Post**: Edita posts existentes.
- **Eliminar Post**: Elimina posts.
- **Registrar**: Registro de nuevos usuarios.
- **Iniciar Sesión**: Inicio de sesión para usuarios registrados.
- **Perfil**: Página de perfil del usuario para actualizar información.

## Contribución

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva característica'`).
4. Empuja a tu rama (`git push origin feature/nueva-caracteristica`).
5. Crea una Pull Request.
