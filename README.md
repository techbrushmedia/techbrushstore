

<h1 align="center">TechBrush Store</h1>

<p align="center">
  A polished Django storefront for browsing products, managing a cart, and placing delivery orders.
</p>

<p align="center">
  <a href="https://www.djangoproject.com/"><img src="https://img.shields.io/badge/Django-5.2-0C4B33?logo=django&logoColor=white" alt="Django 5.2"></a>
  <a href="https://tailwindcss.com/"><img src="https://img.shields.io/badge/Tailwind_CSS-3.4-06B6D4?logo=tailwindcss&logoColor=white" alt="Tailwind CSS 3.4"></a>
  <a href="license.txt"><img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License"></a>
</p>

<p align="center">
  <a href="#features">Features</a> &bull;
  <a href="#quick-start">Quick Start</a> &bull;
  <a href="#store-management">Store Management</a> &bull;
  <a href="#technology">Technology</a>
</p>

---

## Overview

TechBrush Store is a responsive e-commerce application built for a straightforward shopping journey: discover products, choose available variants, build a cart, and submit a delivery order. Store owners manage the catalogue, customer orders, contact requests, and storefront content through Django admin.

The project is a substantially modified and extended version of Nixagone, originally created by Mohin Uddin Shipon.

## Features

### Product Discovery

| Capability | Details |
| --- | --- |
| Catalogue | Browse active products in configurable pages of 8, 12, or 24 items. |
| Search and filters | Search names, categories, and descriptions; filter by category and price range. |
| Sorting | Sort by name, price, or newest products. |
| Product details | View descriptions, imagery, stock availability, size and colour variants, and related products. |
| Merchandising | Highlight selected products on the home page. |

### Cart and Checkout

| Capability | Details |
| --- | --- |
| Guest cart | Visitors can build a cart before creating an account. |
| Stock protection | Product availability is checked when items are added and again during checkout. |
| Variant selection | Required size and colour selections are validated before adding an item. |
| Cart controls | Increase or decrease quantities, remove items, and review the subtotal. |
| Delivery order | Capture delivery name, email, phone number, address, and district. |
| Shipping costs | Apply a dedicated delivery cost for Dhaka and a standard cost for other districts. |

### Customer and Store Operations

* Register, sign in, sign out, and reset a password.
* Confirm a guest order using a session-protected confirmation page.
* Let authenticated customers view their order history, inspect order details, and cancel pending or confirmed orders.
* Track order and payment statuses through Django admin. Payment status tracking is included; no online payment gateway is implemented.
* Collect customer enquiries with a contact form.
* Publish About, shipping and returns, privacy, and terms pages.
* Expose `robots.txt` through `django-robots`.

## Shopping Flow

```text
Browse catalogue -> Select product and variant -> Add to cart -> Checkout
       -> Enter delivery details -> Confirm order -> Track order status
```

## Quick Start

### Prerequisites

* Python 3
* Node.js and npm (only for front-end dependencies)
* SQLite for local development, or PostgreSQL for a production database

### Install

```sh
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

npm install
```

### Configure

Create a `.env` file in the project root:

```env
SECRET_KEY=replace-with-a-strong-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

`DATABASE_URL` is read with `dj-database-url`. SQLite is suitable for local development; use a PostgreSQL URL for production.

### Run

```sh
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to browse the storefront, or [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to manage it.

## Store Management

Use Django admin to configure the store identity and operations:

* Store name, contact information, social links, and About content.
* Home-page image and delivery costs.
* Categories, products, product images, available sizes, and colours.
* Product stock, featured products, orders, users, and contact messages.

Prices and delivery costs are stored as integers. Adapt labels and currency formatting in the templates when decimal amounts are required.

## Project Structure

```text
apps/
  cart/         # Cart and cart-item logic
  order/        # Addresses, orders, and checkout
  product/      # Categories, products, variants, and images
main/           # Users, storefront content, and configuration
nix/            # Django settings and project URLs
templates/      # Django templates
static/         # Stylesheets, JavaScript, and image assets
media/          # Images uploaded through the admin
```

## Front-end Development

The interface uses Tailwind CSS and Alpine.js. Application assets are located in `static/`, Tailwind configuration is in `tailwind.config.js`, and Django templates are in `templates/`.

## Deployment

Before deployment, use a strong `SECRET_KEY`, set `DEBUG=False`, configure the appropriate `ALLOWED_HOSTS`, provide a production `DATABASE_URL`, and arrange static and media file serving. Then collect static assets:

```sh
python manage.py collectstatic
```

## Technology

* [Django](https://www.djangoproject.com/)
* [Tailwind CSS](https://tailwindcss.com/)
* [Alpine.js](https://alpinejs.dev/)
* [django-robots](https://github.com/jazzband/django-robots)
* [Pillow](https://python-pillow.org/)

## Attribution and License

Nixagone was created by Mohin Uddin Shipon and released under the MIT License. TechBrush has made significant changes to the interface, structure, and functionality.

Copyright notices and the license must be retained when redistributing the software. See [license.txt](license.txt) for the complete license text.

<p align="center">TechBrush &middot; <a href="https://techbrush.fr">techbrush.fr</a></p>
# TechBrush Store

TechBrush's Django e-commerce application. It provides a product catalogue, shopping cart, and delivery order flow.

This project is a substantially modified and extended version of Nixagone, originally created by Mohin Uddin Shipon.

## Features

### Catalogue

* Active product listing with configurable pagination: 8, 12, or 24 products per page.
* Search across product names, categories, and descriptions.
* Category and price-range filters.
* Sorting by name, price ascending, price descending, or newest products.
* Product pages with descriptions, images, size and colour variants, available stock, and related products.
* Featured products on the home page.

### Cart and Orders

* Cart available to both visitors and authenticated users.
* Product and variant selection with stock checks and required-option validation.
* Quantity updates, item removal, and subtotal calculation.
* Delivery form for name, email, phone number, address, and district.
* Delivery costs calculated differently for Dhaka and other districts.
* Order confirmation available to the guest who placed the order, plus order management for authenticated users.
* Customer order history, order details, and order cancellation.

### Accounts and Content

* Registration, sign-in, sign-out, and password reset.
* About page, contact form, and shipping/returns, privacy, and terms pages.
* Store configuration through the admin: contact information, social links, content, home-page image, and delivery costs.
* Responsive interface built with Tailwind CSS and Alpine.js.
* Django admin for products, categories, orders, users, and contact messages.
* `robots.txt` endpoint for search-engine indexing.

## Project Structure

```text
apps/
  cart/         # cart and cart items
  order/        # addresses, orders, and checkout
  product/      # categories, products, variants, and images
main/           # users, content, and store configuration
nix/            # Django project configuration and URLs
templates/      # Django templates
static/         # stylesheets and scripts
media/          # images uploaded through the admin
```

## Local Installation

### 1. Create the Python Environment

```sh
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=replace-this-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

`DATABASE_URL` is read through `dj-database-url`. SQLite is suitable for local development; a PostgreSQL URL can be used in production.

### 3. Initialize the Database

```sh
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run the Server

```sh
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. The admin site is available at `http://127.0.0.1:8000/admin/`.

## Store Configuration

Use the admin site to create or edit the store configuration, including its name, contact information, social links, About content, home-page image, and delivery costs. Then add categories, products, images, and variants to populate the catalogue.

Prices and delivery costs are stored as integers. Adapt the labels and currency formatting in the templates if your currency requires decimal values.

## Front-end Development

Tailwind CSS is declared in `package.json`. Install front-end dependencies with:

```sh
npm install
```

Interface styles and scripts are in `static/`, the Tailwind configuration is in `tailwind.config.js`, and views are in `templates/`.

## Deployment

Before deployment, set a strong secret key, `DEBUG=False`, appropriate allowed hosts, and a production database. Also configure static and media file serving, then run:

```sh
python manage.py collectstatic
```

## Technologies

* [Django](https://www.djangoproject.com/)
* [Tailwind CSS](https://tailwindcss.com/)
* [Alpine.js](https://alpinejs.dev/)
* [django-robots](https://github.com/jazzband/django-robots)

## Attribution and License

Nixagone was created by Mohin Uddin Shipon and released under the MIT License. TechBrush has made significant changes to the interface, structure, and functionality.

Copyright notices and the license must be retained when redistributing the software. See [license.txt](license.txt) for the full license text.

TechBrush : https://techbrush.fr
