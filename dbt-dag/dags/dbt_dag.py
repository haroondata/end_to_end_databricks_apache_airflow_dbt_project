import os
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import DatabricksTokenProfileMapping

# Profile Configuration
profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=DatabricksTokenProfileMapping(
        conn_id="databricks_conn", 
        profile_args={
            "database": "tpch", 
            "schema": "tpch",
        },
    )
)

# dbt DAG Definition
dbt_databricks_dag = DbtDag(
    dag_id="dbt_databricks_dag",
    project_config=ProjectConfig(f"{os.environ['AIRFLOW_HOME']}/dbt-dag/dags/dbt/datapipeline"),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}\\dbt_venv\\Scripts\\dbt"
    ),
    schedule_interval="@daily",
    start_date=datetime(2024, 12, 21),
    catchup=False,
)