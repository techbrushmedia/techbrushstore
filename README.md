# Nixagone — TechBrush Edition

Nixagone is a modern, customizable e-commerce web application built with Django.

This repository is a **significantly modified and further developed version of the original Nixagone project**, with substantial modifications, improvements, redesigns, and additional functionality developed by **TechBrush**.

> **Original project:** Nixagone by Mohin Uddin Shipon
> **Further development:** TechBrush

---

## Features

* **Product Catalog**: Browse, search, and filter products by category.
* **Shopping Cart**: Add, update, and remove products from the cart.
* **Order Management**: Checkout process with delivery cost calculation.
* **Custom User Model**: Extensible user authentication.
* **Admin Dashboard**: Manage products, orders, and users.
* **Responsive Design**: Mobile-friendly UI using Tailwind CSS and Alpine.js.
* **SEO & Social**: Robots.txt, meta tags, and social links in the footer.
* **Environment-based Settings**: Uses `.env` for secrets and database configuration.

---

## Project Structure

```text
apps/
  cart/         # Cart logic and models
  order/        # Order processing and checkout
  product/      # Product catalog and categories
main/           # Main app: users, forms, views, etc.
nix/            # Django project settings, URLs, WSGI/ASGI
static/         # CSS, JS, images
templates/      # HTML templates
media/          # Uploaded product images
```

---

## Getting Started

### 1. Clone & Install

```sh
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Environment Setup

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### 3. Database & Static Files

```sh
python manage.py migrate
python manage.py collectstatic
```

### 4. Run the Server

```sh
python manage.py runserver
```

Visit:

`http://127.0.0.1:8000`

---

## Customization

* **Site Title & Configuration**: Configure through Django admin or project settings.
* **Styling**: Edit `static/css/main.css` and `tailwind.config.js`.
* **JavaScript**: Interactivity is powered by Alpine.js.
* **Templates**: Customize the templates in the `templates/` directory.

---

## Deployment

For production:

* Set `DEBUG=False`.
* Configure `ALLOWED_HOSTS`.
* Use PostgreSQL or another production database.
* Configure static and media file serving.
* Store secrets securely using environment variables.

---

## Credits & Attribution

### Original Project

**Nixagone** was originally created by **Mohin Uddin Shipon**.

This project is based on the original Nixagone software, which was released under the MIT License.

### Further Development

**TechBrush**

TechBrush has significantly modified and further developed the original project, including substantial changes to the application, user interface, functionality, structure, and overall design.

Copyright for the original Nixagone software remains with its original author.

Copyright for original modifications and contributions made by TechBrush belongs to TechBrush.

Website: https://techbrush.fr

---

## Third-Party Technologies

This project uses or may use third-party technologies including:

* [Django](https://www.djangoproject.com/)
* [Tailwind CSS](https://tailwindcss.com/)
* [Alpine.js](https://alpinejs.dev/)

Each third-party technology is subject to its own license and terms.

---

## License

This project is distributed under the **MIT License**.

The original Nixagone software is Copyright © 2025 Mohin Uddin Shipon.

Significant modifications and additional contributions are Copyright © 2026 TechBrush.

See the [`LICENSE`](LICENSE) file for the complete license text and copyright notices.

---

## Attribution

If you redistribute this software or substantial portions of it, please retain the copyright notices and license included with the project.

**Original project:** Nixagone — Mohin Uddin Shipon
**Modified and further developed by:** TechBrush
TechBrush: https://techbrush.fr

---

**Happy coding!**
