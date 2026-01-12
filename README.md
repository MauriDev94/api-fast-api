
### To activate Python virtual environment
*windows bash
```bash
    venv/scripts/activate
```

### Install Dependencies
```bash
    pip install -r requirements.txt
```

### Run Postgres DB in Docker
1. Run Postgres DB container
```bash
    docker-compose -f docker-compose-dev.yaml --env-file .env up -d
```

### Run the application
```bash
    uvicorn app.main:app --reload
```

### Alembic Command
0. Initialize alembic
```bash
    alembic init alembic
```
1. Create migration
```bash
    alembic revision --autogenerate -m "your message..."
```
2. Update database
```bash
    alembic upgrade head
```
3. This will undo the last migration
```bash
    alembic downgrade -1
```
4. This will list all migration history(You can use this to find the migration to undo)
```bash
    alembic history --verbose
```
5. Downgrade to specific revision
```bash
    alembic downgrade <revision ID>
```
6. This will reset the database to the initial state
```bash
    alembic downgrade base
```


