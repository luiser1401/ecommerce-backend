# ecommerce-backend

A FastAPI-based e-commerce backend using clean architecture principles.

## Project Structure

The project follows a clean architecture approach with three main layers:

- **Web Layer**: Handles HTTP requests and responses
  - API routes
  - Request/response schemas
  - Middleware

- **Service Layer**: Contains business logic
  - Use cases
  - Service interfaces
  - Domain models

- **Data Layer**: Manages data persistence
  - Repositories
  - Data models
  - Data sources

## Directory Structure

```
ecommerce-backend/
├── app/
│   ├── web/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   └── schemas/
│   ├── service/
│   │   ├── interfaces/
│   │   └── usecases/
│   └── data/
│       ├── models/
│       ├── repositories/
│       └── datasources/
├── rc/
│   └── config.py
├── tests/
├── pyproject.toml
└── README.md
```

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -e .
   ```
3. Run the development server:
   ```
   uvicorn app.main:app --reload
   ```

## Development

The project uses modern Python tooling:
- FastAPI for the web framework
- SQLAlchemy for database operations
- Pydantic for data validation
- pytest for testing

To run tests:
```
pytest
```
