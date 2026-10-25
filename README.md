# Students Database CRUD Application

An individual backend development project built for EWB Edu Tech Pvt. Ltd. to manage student records using FastAPI and persistent SQLite storage.

---

## 1. Project Objective
The objective of this application is to implement a robust, reliable RESTful API providing full Create, Read, Update, and Delete (CRUD) operations on student profiles.

---

## 2. Technologies Used
- **Python 3**
- **FastAPI**: Modern, high-performance web framework for building APIs.
- **SQLite & SQLAlchemy**: Lightweight, persistent relational database and ORM.
- **Pydantic**: Data validation and type enforcement.
- **Pytest & HTTPX**: Automated, headless API test suite.

---

## 3. Student Record Fields
Each student record contains:
- `id` (Integer, Primary Key): Unique auto-incremented identifier.
- `name` (String): Full name of the student.
- `dob` (String): Date of birth (`YYYY-MM-DD`).
- `email` (String, Unique): Contact email address.
- `phone` (String): Contact phone number.
- `course` (String, Optional): Enrolled academic track.

---

## 4. API Endpoints

| Method | Endpoint | Purpose | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Root | Returns service welcome message. |
| `POST` | `/students` | Create | Adds a new student record (prevents duplicate emails). |
| `GET` | `/students` | Read (All) | Lists all enrolled student records. |
| `GET` | `/students/{student_id}` | Read (Single) | Retrieves a specific student by ID (returns 404 if not found). |
| `PUT` | `/students/{student_id}` | Update | Modifies existing details for a student. |
| `DELETE` | `/students/{student_id}` | Delete | Deletes a student profile from the database. |

---

## 5. Prerequisites & Installation
### Prerequisites
- Python 3.8+
- Git
