# Kopilism Café — Django Web App

A full-featured café website with menu browsing, table reservations, ordering, and payment.

---

## Project Structure

```
kopilism/
├── kopilism/          # Django project config (settings, urls, wsgi)
├── menu/              # Menu items & categories
├── reservations/      # Table reservation booking
├── orders/            # Cart, checkout, payment, order-ready receipt
├── templates/         # HTML templates
│   ├── base.html
│   ├── menu/
│   ├── reservations/
│   └── orders/
├── static/
│   ├── css/main.css
│   └── js/main.js
├── manage.py
└── requirements.txt
```

---

## Setup in VSCode

### 1. Install Python & create virtual environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run migrations (creates database + seeds menu items)
```bash
python manage.py makemigrations menu reservations orders
python manage.py migrate
```

### 4. Create an admin account
```bash
python manage.py createsuperuser
```

### 5. Run the development server
```bash
python manage.py runserver
```

### 6. Open in browser
- **Website:** http://127.0.0.1:8000/
- **Admin panel:** http://127.0.0.1:8000/admin/

---

## Pages

| URL | Description |
|-----|-------------|
| `/` | Landing page (hero, menu preview, reservation CTA) |
| `/menu/` | Browse menu by category |
| `/menu/?category=coffee` | Filter by category (coffee / noncoffee / pastries / meals) |
| `/reservations/` | Table reservation form |
| `/orders/checkout/` | Cart review + payment method selection |
| `/orders/ready/<id>/` | Order status + receipt (auto-polls until ready) |
| `/admin/` | Django admin — manage menu, orders, reservations |

---

## How the Order Flow Works

1. Customer browses `/menu/` and adds items to cart (stored in browser `sessionStorage`)
2. Goes to `/orders/checkout/` — reviews order, selects payment method
3. Clicks **Place Order** — sends cart to Django via POST `/orders/place/`
4. Django creates the `Order` + `OrderItem` records, returns `order_id`
5. Customer is redirected to `/orders/ready/<id>/` — shows "Preparing" screen
6. Staff marks order as ready from **Django Admin** → Orders → change status to **Ready to Serve**
7. The ready page **auto-polls** every 5 seconds and flips to the receipt screen when status = ready

---

## Payment Methods Supported

- **Cash on Hand** — paid at counter when order is ready
- **GCash** — online wallet
- **PayPal** — online wallet
- **Credit Card** — card payment

> Payment is only collected when the order is ready to serve.

---

## Admin Panel Tips

- **Menu → Menu Items** — add/edit items, toggle availability, upload photos
- **Orders → Orders** — change order status to "Ready to Serve" to trigger receipt screen
- **Reservations → Reservations** — view and confirm/cancel bookings

---

## Customization

| What | Where |
|------|-------|
| Café name / tagline | `templates/base.html` |
| Colors | `static/css/main.css` (CSS variables at top) |
| Menu items | Django Admin or `menu/migrations/0002_seed_menu.py` |
| Opening hours | `templates/reservations/reservation.html` |
| Payment methods | `orders/models.py` `PAYMENT_CHOICES` + checkout template |
