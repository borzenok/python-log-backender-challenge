# By borzenok

## Project Structure and Improvements

### User Model Improvements:
- Added UserManager for user management
- Added PermissionsMixin inheritance 
- Added full_name, get_short_name, get_full_name methods
- Added email validation

### Admin Panel Improvements:
- Extended UserAdmin with additional fields
- Added filters and search
- Configured fieldsets for creation and editing

### Added REST API:
- Configured DRF in settings.py
- Created serializers for users
- Added UserViewSet with CRUD operations
- Added /me/ endpoint
- Added API documentation (Swagger/ReDoc)

### Added Service Layer Architecture:
- Created UserService for business logic
- Added selectors for query optimization
- Implemented separation of concerns

### Added Tests:
- User model tests
- API endpoint tests
- Service layer tests

### Added Additional Components:
- Constants (UserRole)
- Validators
- Custom permissions (IsOwnerOrAdmin)

These changes are aimed at creating a more reliable, testable, and scalable application with clear architecture and good documentation.

# Die Hard

This is a project with a test task for backend developers.

You can find detailed requirements by clicking the links:
- [English version](docs/task_en.md)
- [Russian version](docs/task_ru.md)

Tech stack:
- Python 3.13
- Django 5
- pytest
- Docker & docker-compose
- PostgreSQL
- ClickHouse

## Installation

Put a `.env` file into the `src/core` directory. You can start with a template file:

```
cp src/core/.env.ci src/core/.env
```

Run the containers with
```
make run
```

and then run the installation script with:

```
make install
```

## Tests

`make test`

## Linter

`make lint`
