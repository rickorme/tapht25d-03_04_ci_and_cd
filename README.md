# tapht25d-03_04_ci_and_cd

## Discussion points

### 1. Advantages of CI & CD

> What advantages can you see with CI (Continuous Integration) & CD (Continuous Delivery/Deployment) at your workplace?
If you are not currently working: How would you like this to function at your future workplace?

### 2. The Purpose of Linting

> What is the point of linting?

### 3. Git Workflow in Teams

> How do you work with Git and multiple branches within a team?

### 4. Pull Requests

> What is a pull request (PR)?


## Install requirements
``` bash
pip install -r requirements.txt
```

## Run Flake8 linter
``` bash
flake8 src tests
```

## Run unit tests
``` bash
pytest -m unit
```

## Run integartion tests
``` bash
pytest -m integration
```