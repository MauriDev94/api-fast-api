### VS Code Setup
1. Install python extension
2. Install Pylance extension
3. Install autoDocstring - python Docstring Generator 
4. Install Code Spell Checker
5. Install Black Formatter


### To Activate Python Virtual Environment
### VS Code Setup
1. Install python extension
2. Install Pylance extension
3. Install autoDocstring - python Docstring Generator 
4. Install Code Spell Checker
5. Install Black Formatter


### To Activate Python Virtual Environment

'''bash
    .venv\scripts\activate
    .venv\scripts\activate
'''

### To deactivate venv

'''Bash
    deactivate
    deactivate
'''


### Install Dependencies

´´´bash
    pip install -r requirements.txt
    pip install -r requirements.txt
'''


### Run the Application
'''bash
    uvicorn main:app --reload
'''


### Run Postgres DB in docker
1. Run Postgres DB Container
'''bash
    docker compose -f docker-compose-dev.yaml --env-file .env up -d
'''


### Alembic Commands

0. Initialize alembic
'''bash
    alembic init alembic
'''
1. Create migration
'''bash
    alembic revision --autogenerate -m "your message..."
'''
2. Update database
'''bash
    alembic upgrade heady
'''
3. this will undo the last migration
'''bash
    alembic downgrade -1
4. this will list all migration history(you can use this to find the migration to undo)
'''bass
alembic history --verbose
'''