# Django Employee-Department App

A simple Django project that demonstrates how to work with relational database models and display data dynamically in HTML templates.

---

## 🧩 Features

- Department, Employee, and Salary Grade models
- Data displayed via Django views and templates
- Example usage of ForeignKey and Self-referential relationships
- Organized and modular Django app structure

---

## 🏗️ Project Structure

```
project_root/
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── display_dept.html
│   │   ├── display_emp.html
│   │   └── display_salgrade.html
│   └── __init__.py
│
├── project_name/
│   ├── urls.py
│   ├── settings.py
│   └── __init__.py
│
├── manage.py
└── db.sqlite3
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/django-employee-department-app.git
cd django-employee-department-app
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux
```

### 3️⃣ Install dependencies
```bash
pip install django
```

### 4️⃣ Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the server
```bash
python manage.py runserver
```

Visit 👉 http://127.0.0.1:8000/display_dept/, /display_emp/, or /display_salgrade/.

---

## 🧑‍💻 Models Overview

- **Dept** — Department details (`deptno`, `dname`, `loc`)
- **Emp** — Employee details (`empno`, `ename`, `job`, `mgr`, `deptno`, etc.)
- **Salgrade** — Salary grade info (`grade`, `low_sal`, `high_sal`)

---

## 🧾 License

This project is open source and available under the [MIT License](LICENSE).
