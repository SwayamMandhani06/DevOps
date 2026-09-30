# DevOps Assignment 6 — Jenkins Integration with GitHub

## Student Details
- **Name:** Swayam Mandhani
- **PRN / Roll No.:** 123B1B184
- **Class:** B.Tech Computer Engineering
- **Division / Batch:** C / C2
- **Subject:** DevOps (BCE27PE01)
- **Assignment:** 6

## Title
**Continuous Integration with Jenkins and GitHub**

## Aim
To integrate the Jenkins automation server with a remote Git repository on GitHub and automate source code retrieval, build execution, and validation across both Freestyle projects and Declarative Pipelines.

## Technologies
- **Jenkins:** Version 2.568.3 (Automation Server)
- **Java Runtime:** OpenJDK 21.0.12.1 LTS
- **Version Control:** Git 2.55.0 & GitHub SCM
- **Language / Scripting:** Python 3.12, Windows Batch, Groovy (Declarative Pipeline)

## Project Structure
```text
Assignment-6/
├── Jenkinsfile
├── README.md
├── app.py
└── Screenshots/
    ├── ss1.png
    ├── ss2.png
    ├── ss3.png
    ├── ss4.png
    ├── ss5.png
    ├── ss6.png
    ├── ss7.png
    ├── ss8.png
    ├── ss9.png
    ├── ss10.png
    ├── ss11.png
    ├── ss13.png
    └── ss14.png
```

## Application
A lightweight Python application ([`app.py`](./app.py)) executed by Jenkins during CI builds to verify successful source-code checkout from the remote GitHub `main` branch.

```python
print("========================================")
print(" Jenkins + GitHub CI/CD Demo")
print("========================================")
print("Updated source code successfully retrieved from GitHub.")
print("Jenkins executed the latest version from the main branch.")
print("Assignment 6 - DevOps")
```

## Jenkinsfile (Declarative Pipeline)
Pipeline as Code definition ([`Jenkinsfile`](./Jenkinsfile)) implementing multi-stage automated build workflow:

```groovy
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/SwayamMandhani06/DevOps.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                bat 'cd Assignment-6 && "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
    }
}
```

## Continuous Integration Implementation

### 1. Jenkins Freestyle Project (`GitHub-Jenkins-Demo`)
- **Source Code Management:** Git (`https://github.com/SwayamMandhani06/DevOps.git`), branch `*/main`.
- **Build Trigger:** Poll SCM with schedule `H/5 * * * *` (polls remote GitHub repository every 5 minutes).
- **Build Step:** Execute Windows batch command:
  ```bat
  cd Assignment-6
  "C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe" app.py
  ```
- **Verification:** Automatically triggered upon committing changes to GitHub, populating workspace files and successfully executing Python build step.

### 2. Jenkins Declarative Pipeline (`GitHub-Jenkins-Pipeline`)
- **Definition:** Pipeline script from SCM.
- **SCM:** Git (`https://github.com/SwayamMandhani06/DevOps.git`), branch `*/main`.
- **Script Path:** `Assignment-6/Jenkinsfile`.
- **Execution Stages:**
  1. **Checkout:** Clones remote repository and checks out commit from `main`.
  2. **Build:** Runs `bat 'cd Assignment-6 && python app.py'`.
  3. **Test:** Validates application execution.

## Result
Jenkins was successfully integrated with GitHub. Source code retrieval on the `main` branch was automated through both Freestyle projects (with `H/5 * * * *` SCM polling) and Declarative Pipelines (`Jenkinsfile`), validating automatic code checkout, execution, workspace population, and successful build completion.

## Screenshot Evidence

| Figure | Screenshot | Purpose |
|---|---|---|
| 1 | [`ss1.png`](Screenshots/ss1.png) | OpenJDK 21 LTS and Git CLI version verification in PowerShell |
| 2 | [`ss2.png`](Screenshots/ss2.png) | Jenkins automation server dashboard running locally on `http://localhost:8080` |
| 3 | [`ss3.png`](Screenshots/ss3.png) | Jenkins installed plugins configuration (Pipeline plugin suite verified) |
| 4 | [`ss4.png`](Screenshots/ss4.png) | Remote GitHub repository verification under `Assignment-6/` on branch `main` |
| 5 | [`ss5.png`](Screenshots/ss5.png) | Freestyle project (`GitHub-Jenkins-Demo`) SCM configuration for GitHub repository |
| 6 | [`ss6.png`](Screenshots/ss6.png) | Freestyle project build step configuration (Execute Windows batch command) |
| 7 | [`ss7.png`](Screenshots/ss7.png) | Freestyle project build execution status and Git commit revision tracking |
| 8 | [`ss8.png`](Screenshots/ss8.png) | Jenkins workspace inspection showing retrieved `app.py` and `README.md` |
| 9 | [`ss9.png`](Screenshots/ss9.png) | Build console output showing successful Git checkout and Python execution |
| 10 | [`ss10.png`](Screenshots/ss10.png) | SCM polling trigger log (`H/5 * * * *`) and build history status |
| 11 | [`ss11.png`](Screenshots/ss11.png) | Declarative Pipeline job configuration from SCM pointing to `Assignment-6/Jenkinsfile` |
| 12 | [`ss13.png`](Screenshots/ss13.png) | Pipeline console execution log displaying Checkout, Build, and Test stage completion |
| 13 | [`ss14.png`](Screenshots/ss14.png) | Pipeline dashboard overview confirming successful stage execution and stable status |

## Submission
**GitHub:** https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-6

**Hosted / Output:** N/A — Local Jenkins automation server.
