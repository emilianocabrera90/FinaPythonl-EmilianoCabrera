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

* Home: http://127.0.0.1:8000/
* Blog: http://127.0.0.1:8000/post/<id>/
* Crear Post: http://127.0.0.1:8000/post/new/
* Editar Post: http://127.0.0.1:8000/post/<id>/edit/
* Eliminar Post: http://127.0.0.1:8000/post/<id>/delete/
* Registro de Usuario : http://127.0.0.1:8000/accounts/signup/
* Login: http://127.0.0.1:8000/accounts/login/
* Perfil: http://127.0.0.1:8000/accounts/profile/
* Admin: http://127.0.0.1:8000/admin/

## Contribución

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva característica'`).
4. Empuja a tu rama (`git push origin feature/nueva-caracteristica`).
5. Crea una Pull Request.
