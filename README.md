

# Anonymous Posting App

A collaborative practice project built to improve teamwork and gain hands-on experience with full-stack web development using Django.


(This project is beginner-friendly and is intended as a learning experience rather than a production-ready application)

---

## Features

### Anonymous Users

* Create posts without creating an account
* Comment on posts
* Delete their own posts
* Delete their own comments

### Admin

* Manage posts
* Manage comments
* Dashboard with project statistics

  * Total posts
  * Posts created today

---

## Tech Stack

### Frontend

* Django Templates
* Tailwind CSS

### Backend

* Django

### Database

* PostgreSQL

----------------------------------
----------------------------------

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd AnonymousPostingApp
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Node dependencies

```bash
npm install
```

### 5. Create a `.env` file

Example:

```env
SECRET_KEY=your-secret-key

DB_NAME=anonymous_posting
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Start Tailwind CSS

```bash
npm run dev
```

### 8. Start the Django development server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## Development Status

### Completed

* Django project setup
* PostgreSQL integration
* Environment configuration
* Anonymous posting system
* Anonymous commenting system
* Owner-only deletion
* Django Admin
* Simple admin dashboard
* Tailwind CSS integration

### Planned

* Responsive UI redesign
* Improved dashboard
* Search and filtering
* Pagination
* Better user experience
* Production deployment

---

## Collaborators

* Debian
* ~~~

---

## License

This project is licensed under the MIT License.



________        ___.   .__               
\______ \   ____\_ |__ |__|____    ____  
 |    |  \_/ __ \| __ \|  \__  \  /    \ 
 |    `   \  ___/| \_\ \  |/ __ \|   |  \
/_______  /\___  >___  /__(____  /___|  /
        \/     \/    \/        \/     \/ Apes together strong