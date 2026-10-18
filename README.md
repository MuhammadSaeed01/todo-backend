# To-Do App — Django Backend

Replaces the old Express/Node backend. Runs on **http://localhost:8000**.

## Setup

```bash
# 1. Install dependencies (already done if packages exist)
pip install -r requirements.txt

# 2. Apply database migrations
python manage.py migrate

# 3. Seed initial data (run once)
python seed.py

# 4. Start the dev server
python manage.py runserver 8000
```

## API Endpoints

| Method | URL                              | Description            |
|--------|----------------------------------|------------------------|
| GET    | /api/tasks                       | Get all tasks          |
| GET    | /api/tasks/category/\<category\> | Get tasks by category  |
| POST   | /api/tasks                       | Create a new task      |
| PUT    | /api/tasks/\<id\>                | Update a task          |
| DELETE | /api/tasks/\<id\>                | Delete a task          |

### POST / PUT body (JSON)

```json
{
  "category": "Personal",   // Personal | Work | Academic
  "text": "Buy grocery",
  "completed": false
}
```

## Notes

- Database: SQLite (`db.sqlite3`) — no extra setup needed.
- CORS is open to all origins in development (`CORS_ALLOW_ALL_ORIGINS = True`).  
  Restrict this before going to production.
- Change `SECRET_KEY` in `settings.py` before deploying.
