# tapht25d-03_04_ci_and_cd

## Discussion points

### 1. Advantages of CI & CD

> What advantages can you see with CI (Continuous Integration) & CD (Continuous Delivery/Deployment) at your workplace?

On a recent stusy group project, we worked with branch protection rules which required a CI pipeline to have successfully completed before a PR could be merged. The pipeline included several layers of automated testing including:

    - Linting
    - Various security scans (Dependency vulnerability scanning, Static Applicatoin Security Testing and Secrets Detection)
    - Automated testing: Unit, Integration, API and End-to-End testing

#### Advantages

- Although automated testing takes some work to set up, ultimately it saves a huge amount of time as the tests need to be run every time the codebase changes. 
- By including security scans in a CI pipeline, security issues can be detected much earlier than in traditional development cycles. This "shift-left" philosophy in software development leads to security issues being detected much earlier in the cycle which ultimately leads to easier and cheaper remediation, and a higher standard of delivered software.
- Shifting to IaC (infrastructure as Code): coding and versioning deployments means that they are consistent and auditable. Human error is greatly reduced and the speed of deployment is increased. Scaling and disaster recovery are also much easier when deployments can be automated this way.

### 2. The Purpose of Linting

> What is the point of linting?

Linting helps to ensure a certain level of standaradisation of code across a team which. Because of the consistency enforces, the codebase becomes easier to read. Linters also help to keep the codebase clean, more secure and less buggy by detecting things like imports and variables which are not actually used in the code.

### 3. Git Workflow in Teams

> How do you work with Git and multiple branches within a team?

- In my most recent project I worked with the GitHub Flow branching strategy. We created feature branches from the main branch to work on new features or fixes. Once a feature/fix was deemed complete, the developer would create a PR (pull request) which required a review from at least one other developer before the changes could be merged into the main branch. 

### 4. Pull Requests

> What is a pull request (PR)?

A PR is a request to merge one code bracnh into another - e.g. a feature branch into the main branch. This provides an opportunity to discuss the changes and suggest improvements with another team member. A PR typically also triggers a CI/CD pipeline to run automated testing.


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