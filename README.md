🧑‍💻 Job Portal Backend API

A role-based backend for a Job Portal built with **Django REST Framework** where

* Employers post jobs
* Job seekers apply
* Employers manage applicants
* Public job search with filtering & pagination

---

🚀 Features

✔ JWT Authentication (access + refresh)
✔ Custom User Model (Employer / Seeker)
✔ Role-Based Permissions
✔ CRUD operations for Jobs
✔ Job Applications with status workflow
✔ Employers see applicants
✔ Seekers track their applications
✔ Search, Filter, Sort + Pagination
✔ Django Admin panel
✔ Fully tested through Postman
✔ PostgreSQL production-ready

---

## 🏗️ Tech Stack

| Layer     | Tools                |
| --------- | -------------------- |
| Language  | Python               |
| Framework | Django + DRF         |
| Database  | PostgreSQL           |
| Auth      | JWT (SimpleJWT)      |
| Filtering | django-filter        |
| Admin     | Django Admin         |
| Tools     | Git, Postman, VSCode |

---

## 📌 Database Schema

### Users

```
User (email login)
- id
- email
- name
- role (EMPLOYER / SEEKER)
```

### Jobs

```
Job
- employer_id -> User
- title, description, location, salary_range
```

### Job Applications

```
JobApplication
- applicant_id -> User
- job_id -> Job
- status (submitted/reviewed/accepted/rejected)
```

---

## 🔑 API Endpoints

### 🔐 Auth

```
POST   /api/auth/register/
POST   /api/auth/login/
POST   /api/auth/token/refresh/
GET    /api/auth/me/
PATCH  /api/auth/me/
```

### 💼 Jobs

```
GET    /api/jobs/
POST   /api/jobs/                     # employer
GET    /api/jobs/<id>/
PUT    /api/jobs/<id>/                # employer
DELETE /api/jobs/<id>/                # employer
```

### 📝 Applications

```
POST   /api/applications/apply/       # seeker
GET    /api/applications/mine/        # seeker
GET    /api/applications/employer/    # employer
PATCH  /api/applications/<id>/update-status/
```

---

## 📥 Request Examples

### Register Employer

```json
POST /api/auth/register/
{
  "email": "owner@gmail.com",
  "name": "Owner",
  "role": "EMPLOYER",
  "password": "Test@123"
}
```

### Create Job (Employer)

```json
POST /api/jobs/
{
  "title": "Django Backend Engineer",
  "description": "REST API developer",
  "location": "Bangalore",
  "salary_range": "6–9 LPA"
}
```

### Apply Job (Seeker)

```json
POST /api/applications/apply/
{
  "job": 1,
  "resume_link": "https://drive.link/resume.pdf"
}
```

---

## 🧪 Testing

📌 Tested using Postman
📌 Token stored as Bearer Token
📌 Includes pagination, search, filtering

---

## 🛠️ Setup Instructions

```bash
git clone <repo-url>
cd job_portal
python -m venv venv
source venv/bin/activate  # windows: venv\Scripts\activate
pip install -r requirements.txt
```

Update DB settings in `core/settings.py`:

```bash
DB = job_portal  USER = postgres  PASS = <your_pass>
```

Run migrations:

```bash
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```

---

## 🗄️ Environment Variables

Create `.env` (optional):

```
DB_NAME=job_portal
DB_USER=postgres
DB_PASSWORD=****
DB_HOST=localhost
SECRET_KEY=<your_django_secret>
DEBUG=True
```

---

## 🌐 Deployment Ready

* Supports Render/Railway/AWS
* Use Gunicorn + Nginx or render built-in
* DB = PostgreSQL

---

## 📁 Project Structure

```
core/
accounts/
jobs/
applications/
...
```

---

## 🚧 Future Enhancements

* Email notifications on hiring status
* Resume file upload (S3/Cloudinary)
* Admin dashboards with charts
* Favorite/bookmark jobs
* Interview scheduling module

---

## ❤️ Owner

**Satya Venkata Narasimha N**
Backend Developer | Python | Django
📧 [venkatnsv6@gmail.com](mailto:venkatnsv6@gmail.com)

---


