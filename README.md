### VS Code Setup
1. Install python extension
2. Install Pylance extension
3. Install autoDocstring - python Docstring Generator 
4. Install Code Spell Checker
5. Install Black Formatter


### To Activate Python Virtual Environment

'''bash
    .venv\scripts\activate
'''

### To deactivate venv

'''Bash
    deactivate
'''


### Install Dependencies

´´´bash
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
