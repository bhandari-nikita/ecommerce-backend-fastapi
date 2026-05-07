# FastAPI E-Commerce Backend API

A backend API for an e-commerce system built using FastAPI, PostgreSQL, and SQLAlchemy.

## Features

- Create products
- Get all products
- Get single product
- Update product
- Delete product

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /products | Get all products |
| GET | /products/{product_id} | Get single product |
| POST | /products | Create product |
| PUT | /products/{product_id} | Update product |
| DELETE | /products/{product_id} | Delete product |

## Installation

Clone the repository:

```bash
git clone https://github.com/bhandari-nikita/ecommerce-backend-fastapi.git
```

Move into project directory:

```bash
cd ecommerce-backend-fastapi
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
uvicorn main:app --reload
```

Server runs at:

```bash
http://127.0.0.1:8000
```

Swagger API docs:

```bash
http://127.0.0.1:8000/docs
```

## Future Improvements

- JWT Authentication
- User management
- Product categories
- Order management
- Payment integration

## Author

Nikita Bhandari