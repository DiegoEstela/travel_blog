# Travel Blog Project

Este es un proyecto de blog de viajes desarrollado en Django.

## Cómo Probar

1. Clona este repositorio.
2. Crea un entorno virtual: `python -m venv venv`.
3. Activa el entorno virtual: `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows).
4. Instala las dependencias: `pip install -r requirements.txt`.
5. Realiza las migraciones: `python manage.py migrate`.
6. Crea un superusuario: `python manage.py createsuperuser`.
7. Inicia el servidor: `python manage.py runserver`.

## Funcionalidades

1. Página Principal

- URL: /
- Descripción: Muestra una lista de todos los posts disponibles.
- Acceso: Puedes ver los posts y explorar el contenido del blog.

2. Crear un Nuevo Autor

- URL: /create_author/
- Descripción: Permite crear un nuevo autor ingresando su nombre y una breve biografía.
- Acceso: Cualquier usuario puede acceder para crear un nuevo autor.

3. Crear una Nueva Categoría

- URL: /create_category/
- Descripción: Permite crear una nueva categoría ingresando su nombre.
- Acceso: Cualquier usuario puede acceder para crear una nueva categoría.

4. Crear un Nuevo Post

- URL: /new_post/
- Descripción: Permite a los usuarios crear un nuevo post ingresando título, contenido y seleccionando categorías relacionadas.
- Acceso: Cualquier usuario puede acceder para crear un nuevo post.

5. Buscar Posts

- URL: /search/
- Descripción: Permite a los usuarios buscar posts según un término de búsqueda específico.
- Acceso: Cualquier usuario puede acceder para buscar contenido en la base de datos.
