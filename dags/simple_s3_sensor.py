from datetime import datetime, timedelta

from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow import DAG

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(year=2024, month=1, day=31),
    "retries": 1,
    "retry_delay": timedelta(minutes=15),
}

# [START DAG]
with DAG(dag_id="simple_s3_sensor", default_args=default_args) as dag:
    # [START TASK]
    sensor = S3KeySensor(
        task_id="new_s3_file_in_foobar-bucket",
        aws_conn_id="aws_localstack",
        bucket_key="staging",
        wildcard_match=True,
        bucket_name="example-bucket",
        poke_interval=120,
    )
    # [END TASK]

# [END DAG]

# [START FLOW]
sensor
# [EMD FLOW]
