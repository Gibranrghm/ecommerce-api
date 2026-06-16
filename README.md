# E-commerce Product API

A RESTful API built with Django REST Framework for managing products and categories in an e-commerce context.

## 🛠️ Tech Stack

- Python 3.x
- Django 4.2
- Django REST Framework 3.16
- SQLite (development database)
- Token Authentication

## ✨ Features

- Full CRUD for Products and Categories
- User registration and token-based authentication
- Ownership permissions (only product owners can edit/delete)
- Search products by name or description
- Filter products by category and availability
- Order products by price, name, or date
- Pagination (5 products per page)
- Request throttling (20/min anonymous, 100/min authenticated)

## 🚀 Getting Started

### 1. Clone the repository
```
git clone https://github.com/Gibranrghm/ecommerce-api.git
cd ecommerce-api
```

### 2. Create and activate virtual environment
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run migrations
```
python manage.py migrate
```

### 5. Create a superuser (optional)
```
python manage.py createsuperuser
```

### 6. Start the server
```
python manage.py runserver
```

## 📌 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/register/ | Register a new user |
| POST | /api/login/ | Login and get token |

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/categories/ | List all categories |
| POST | /api/categories/ | Create a category (auth required) |
| GET | /api/categories/{id}/ | Get a category |
| PUT/PATCH | /api/categories/{id}/ | Update a category (auth required) |
| DELETE | /api/categories/{id}/ | Delete a category (auth required) |

### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/products/ | List all products |
| POST | /api/products/ | Create a product (auth required) |
| GET | /api/products/{id}/ | Get a product |
| PUT/PATCH | /api/products/{id}/ | Update a product (owner only) |
| DELETE | /api/products/{id}/ | Delete a product (owner only) |

## 🔍 Filtering, Searching & Ordering

```
# Search by name or description
GET /api/products/?search=laptop

# Filter by category
GET /api/products/?category=1

# Filter by availability
GET /api/products/?available=true

# Order by price (ascending)
GET /api/products/?ordering=price

# Order by price (descending)
GET /api/products/?ordering=-price

# Combine filters
GET /api/products/?category=1&search=laptop&ordering=-price
```

## 🔐 Authentication

This API uses Token Authentication. Include your token in the request header:

```
Authorization: Token your_token_here
```

## 📄 License
MIT