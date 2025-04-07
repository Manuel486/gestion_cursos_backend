# Proyecto de Gestión de Cursos en Django Rest Framework

Este proyecto es una plataforma de gestión de cursos desarrollada con **Django Rest Framework**. Permite a los usuarios gestionar cursos, incluyendo su creación, edición y eliminación a través de una API RESTful. Además, cuenta con una documentación interactiva generada con **Swagger**.

## Aporte de la IA
Este proyecto ha utilizado IA para los siguientes aspectos:

- **Generación de documentación**: La IA ayudó a crear la estructura inicial del archivo `README.md`, facilitando la documentación del proyecto de manera eficiente.
- **Generación de datos**: Se utiliza IA para generar datos de prueba que permiten simular el entorno de producción, ayudando en el desarrollo y validación de funcionalidades.
- **Análisis de problemas de compatibilidad y logs**: La IA también se emplea para entender problemas de compatibilidad y analizar los logs generados durante la ejecución del proyecto, lo que facilita la resolución de

## Versión Desplegada

Puedes acceder al proyecto desplegado y a la documentación interactiva Swagger en la siguiente URL:

> **[Documentación Swagger del Proyecto Desplegado](https://gestion-cursos-backend.onrender.com/swagger/)**

### Autenticación

Para interactuar con la API, se requiere autenticación para los métodos de `POST-PATH-CREATE-DELETE`. Puedes usar las siguientes credenciales para probar la API directamente desde Swagger:

- **Usuario**: `testUser123`
- **Contraseña**: `Test@1234`

### Rutas http
| **Método HTTP** | **Descripción**                                             | **Uso Común**                                                    |
|:----------------|:------------------------------------------------------------|:-----------------------------------------------------------------|
| `GET`           | Recupera información (datos).                               | Obtener un recurso o una lista de recursos. Ejemplo: Obtener cursos. |
| `POST`          | Crea un nuevo recurso.                                      | Crear un nuevo recurso. Ejemplo: Crear un curso.                |
| `PUT`           | Actualiza o reemplaza un recurso existente.                 | Actualizar un recurso completo. Ejemplo: Actualizar un curso.   |
| `DELETE`        | Elimina un recurso existente.                               | Eliminar un recurso. Ejemplo: Eliminar un curso.                |
