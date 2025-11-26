# Proyecto: PayTrack - Taller 2

## Descripción

Este es un sistema de gestión de pagos desarrollado como parte del Taller 2, que implementa los principios de **Arquitectura Hexagonal** y **REST**. El objetivo principal del sistema es registrar, gestionar y consultar pagos realizados por clientes de una manera estructurada y modular.

## Requisitos

- Python 3.11 o superior
- FastAPI
- Uvicorn
- SQLAlchemy
- Otros paquetes listados en `requirements.txt`

## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/Uribe22/Portafolio-md.git
    cd Portafolio-md/Taller2
    ```

2. **Crear un entorno virtual:**

    - Para Windows:

    ```bash
    python -m venv venv
    .\venv\Scripts\Activate
    ```

    - Para macOS/Linux:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecutar el servidor:**

    ```bash
    uvicorn main:app --reload
    ```

    El servidor debería estar disponible en `http://127.0.0.1:8000`.

## Endpoints disponibles

### `POST /pagos`
- **Descripción:** Registrar un nuevo pago.
- **Parámetros:**
    - `nombre_cliente` (string)
    - `monto` (float)

### `GET /pagos`
- **Descripción:** Listar todos los pagos registrados.

### `GET /pagos/{nombre_cliente}`
- **Descripción:** Buscar pagos realizados por un cliente específico.
- **Parámetros:**
    - `nombre_cliente` (string)

### `DELETE /pagos/{id}`
- **Descripción:** Eliminar un pago registrado.
- **Parámetros:**
    - `id` (string)


## Notas adicionales

- Se ha utilizado **FastAPI** para la creación del servicio REST.
- **SQLAlchemy** se ha empleado para la manipulación de datos.
- El proyecto sigue los principios de **arquitectura hexagonal** con separación clara de responsabilidades.
- La lógica de negocio está completamente separada del framework web.

## Integrantes
- **Andrés González** - 20.907.791-4  
- **Lorena Uribe** - 20.908.387-6
