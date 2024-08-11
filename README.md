# Smart Rule Engine

The Smart Rule Engine is a generative AI-powered rule engine that leverages GPT-4 to provide a chat-based interface for managing rule engines in IoT platforms. Currently, it integrates with Thingsboard, with support for additional platforms to be added in the future.


## Setting up
* Clone repo

    ```bash
    git clone https://github.com/kamran890/smart-rule-engine.git
    cd smart-rule-engine
    ```

* Install python3.11

    https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tar.xz

* Create virtual env

    ```bash
    python3.11 -m venv env
    ```

* Enable virtual env

    ```bash
    source env/bin/activate
    ```

* Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

* Create `.env` file

    ```bash
    cp .env.example .env
    ```

* Update following env

    ```bash
    DEBUG=DEBUG
    ENVIRONMENT=DEV
    AI_API_KEY=AI_API_KEY
    IoT_PLATFORM_API_KEY=IoT_PLATFORM_API_KEY
    IoT_PLATFORM_BASE_URL=IoT_PLATFORM_BASE_URL
    REDIS_ENDPOINT=localhost
    DB_ENDPOINT=localhost
    DB_NAME=DB_NAME
    DB_USER=DB_USER
    DB_PASSWORD=DB_PASSWORD
    SECRET_KEY=SECRET_KEY
    REACT_APP_API_ENDPOINT=http://localhost:8000
    REACT_APP_ENDPOINT=http://localhost:3000
    ```

* Run following containers

  ```bash
  docker-compose up -d db redis
  ```

* Run backend

  ```bash
  ./scripts/run_backend.sh
  ```

* Apply migration

  ```bash
  ./scripts/run_migrations.sh
  ```

* Create core tenant

  ```bash
  ./scripts/create_core_tenant.sh
  ```

* Create core admin user

  ```bash
  ./scripts/create_core_admin_user.sh
  ```

* Run other services in seprate terminals

  ```bash
  ./scripts/run_task_manager.sh
  ./scripts/run_data_subscriber.sh
  ```

* Run frontend

  ```bash
  docker-compose up frontend
  ```

* Run unit tests

  ```bash
  ./scripts/run_test.sh
  ```

# URLs

* Backend: http://localhost:8000

* API Docs: http://localhost:8000/docs

* Frontend: http://localhost:3000

# Contributing to project

As an open-source project, contributions are most welcome:

* Code Contributions: Submit patches to enhance existing features, add new ones, or fix bugs.
* Bug Reports: Help us improve by reporting issues you encounter. Please provide as much detail as possible.
* Patch Reviews: Review and provide feedback on other contributors' patches to ensure quality and consistency.

Your contributions, no matter how small, are valued and help make Smart Rule Engine better for everyone

# License

This project is licensed under the terms of the MIT license.
