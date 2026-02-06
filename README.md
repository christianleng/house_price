# House Price Management Platform

source .venv/bin/activate

## Purpose & Context

This project is a comprehensive **House Price management platform** developed by Christian.L as a learning exercise. It combines:

- **FastAPI backend** for API and business logic
- **React + TailwindCSS frontend** (planned)
- **Machine learning features** for house price prediction and recommendations

The platform serves both as a practical application and preparation for technical interviews. Christian emphasizes **deep conceptual understanding** over just coding solutions, frequently exploring the "why" behind design decisions.

The platform includes:

- Agent management
- Property listings (rent & sale)
- Authentication and authorization systems
- Photo and media management
- Plans to match SeLoger’s functionality

---

## Current State

- Backend API implemented with **FastAPI** using a clean **three-layer architecture**: `controllers`, `services`, `models`.
- Unified authentication system for users and agents with **role-based JWT tokens**.
- PostgreSQL database designed with **SQLAlchemy entities** for agents, properties, photos, features, and users.
- Property system now supports both rental and sale transactions, with proper price fields and image management.
- **Swagger UI** configured with token persistence.
- Security patterns implemented:
  - JWT authentication
  - Bcrypt password hashing
  - Ownership verification for sensitive operations

---

## Key Learnings & Principles

- **FastAPI dependency injection** vs JavaScript manual parameter passing
- **Route ordering**: dynamic routes with path parameters must come after specific routes
- **SQLAlchemy entities vs Pydantic schemas**
- Proper **session management** (commit/rollback)
- Database relationships:
  - One-to-Many & Many-to-Many
  - Junction tables
  - Foreign keys vs relationship objects
  - Avoiding duplicate explosion in joins
- **Security principles**:
  - Ownership verification
  - Role-based authentication scalable across user types

---

## Approach & Patterns

- Conceptual explanations before implementation
- Clean architecture with **separation of concerns**
- Comprehensive **error handling**
- Production-ready patterns:
  - Structured logging
  - Rate limiting
- Modular routing with `APIRouter`
- Consistent Pydantic models for request/response validation

---

## Tools & Technologies

- **Backend:** FastAPI, Python, SQLAlchemy ORM, PostgreSQL, JWT, Bcrypt
- **Frontend:** React, TailwindCSS (planned)
- **Dev Tools:** Docker, VS Code with Black, pgAdmin, Git
- **Others:** Python enums, UTC datetime handling, query parameter validation

---

## Project Structure

```text
app/
├── agents
│   ├── controller.py
│   ├── dependencies.py
│   ├── __init__.py
│   ├── schemas.py
│   └── service.py
├── api.py
├── auth
│   ├── controller.py
│   ├── dependencies.py
│   ├── __init__.py
│   ├── schemas.py
│   ├── security.py
│   └── service.py
├── config.py
├── database
│   ├── core.py
│   └── __init__.py
├── entities
│   ├── agent.py
│   ├── enum.py
│   ├── favorites.py
│   ├── feature.py
│   ├── __init__.py
│   ├── photo.py
│   ├── properties.py
│   └── user.py
├── exceptions.py
├── __init__.py
├── logging_config.py
├── main.py
├── properties
│   ├── controller.py
│   ├── dependencies.py
│   ├── __init__.py
│   ├── schemas.py
│   └── service.py
└── rate_limiting.py
```
