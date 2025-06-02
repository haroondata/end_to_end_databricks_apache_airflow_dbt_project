# 🧱 End-to-End Databricks + dbt + Airflow Project

A complete data engineering pipeline using **Databricks**, **dbt**, and **Apache Airflow**.

This project demonstrates how to build and orchestrate a modern data stack with real-world practices:
- Source ingestion
- Data modeling (staging, marts)
- Reusable macros
- Automated testing
- DAG-based orchestration

---

## 📌 Stack

- **Databricks** – Lakehouse platform for storage and compute  
- **dbt (Data Build Tool)** – SQL-based transformations and testing  
- **Apache Airflow** – DAG scheduler for automation  

---

## 🚀 Features

✅ Raw → staging → mart models  
✅ Source freshness and generic tests  
✅ Custom macros and reusable logic  
✅ Example Airflow DAG for CI/CD  
✅ Production-ready structure and configs  

---

## 🗂️ Project Structure

```
.
├── dags/                # Airflow DAGs
├── dbt/                 
│   ├── models/          # dbt models (sources, staging, marts)
│   ├── macros/          # Custom macros
│   ├── tests/           # Generic and singular tests
│   ├── dbt_project.yml  # dbt config
│   └── packages.yml     # dbt packages
├── airflow/             # Airflow configs and Docker setup
├── docker-compose.yml   # Local Airflow orchestration
└── README.md
```

---

## 🧪 dbt Overview

**Model Layers:**

- `models/sources/` – Raw tables from source systems  
- `models/staging/` – Cleaned and transformed base layer  
- `models/marts/` – Business logic, facts & dimensions  

**Custom Macros & Tests:**

- Macros in `macros/` for DRY SQL  
- Generic tests (e.g., `not_null`, `unique`)  
- Singular test examples  

Run locally:

```bash
dbt run       # build models
dbt test      # run tests
```

---

## 🔄 Airflow Deployment

Airflow orchestrates your dbt jobs using a DAG like:

```python
from airflow.operators.bash import BashOperator

dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command='dbt run --project-dir /dbt',
)

dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command='dbt test --project-dir /dbt',
)

dbt_run >> dbt_test
```

To start locally:

```bash
docker-compose up airflow-init
docker-compose up
```

---

## 📦 Installation & Setup

### 1. Clone the Repo

```bash
git clone https://github.com/haroondata/end_to_end_databricks_apache_airflow_dbt_project.git
cd end_to_end_databricks_apache_airflow_dbt_project
```

### 2. Configure dbt Profile

In `~/.dbt/profiles.yml`:

```yaml
databricks_profile:
  target: dev
  outputs:
    dev:
      type: databricks
      host: <your-databricks-host>
      token: <your-token>
      schema: <your-schema>
      catalog: <your-catalog>
      http_path: <your-http-path>
      threads: 4
```

### 3. Start Airflow (Docker)

```bash
docker-compose up airflow-init
docker-compose up
```

---

## 📬 Contact

Made with 💡 by [Haroon](https://github.com/haroondata)  
Feel free to open an issue or fork this repo for your own projects!

---

## 🌐 Useful Tags

#dbt #databricks #apacheairflow #dataengineering #modernstack #analyticsengineering #etl #opensource
