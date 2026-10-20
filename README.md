# EmpireCodes Command Hub — Backend (Django REST Framework)
Architect: **Anthony Oluwaseun Matthew**

This backend powers the **EmpireCodes Command Hub Mobile App** (running on your iPhone via Expo Go) and will also serve client inquiries from your live web portfolio.

---

### Quick Start (3 Commands)

1. **Create and activate a virtual environment:**
   ```bash
   cd c:\Users\PC\Downloads\empirecodes_edit_now\empirecodes_backend_DRF
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Migrate and seed initial database:**
   ```bash
   python manage.py migrate
   python seed_data.py
   ```

4. **Run the server accessible to your iPhone on your local Wi-Fi:**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

---

### API Endpoints Overview

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/dashboard/` | Full mobile dashboard summary (leads, reviews, SLA vitals) |
| `GET` / `POST` | `/api/leads/` | List and create new client inquiry leads |
| `POST` | `/api/leads/{id}/update_status/` | Update lead status (`new`, `in_progress`, `closed`) |
| `GET` / `POST` | `/api/reviews/` | List reviews (`?approved=true` for public, all for mobile) |
| `POST` | `/api/reviews/{id}/toggle_approval/` | Approve / Unapprove client reviews |
| `POST` | `/api/optimize/` | Operations Research linear programming resource solver |
| `GET` | `/admin/` | Django Administration panel |

