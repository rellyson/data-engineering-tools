from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.amazon.aws.operators.s3 import S3FileTransformOperator

S3_SOURCE_FILE_PATH = "s3://example-bucket/landing/example.txt"
S3_DEST_FILE_PATH = "s3://example-bucket/staging/example.txt"

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(year=2024, month=1, day=31),
    "retries": 1,
    "retry_delay": timedelta(minutes=15),
}

# [START DAG]
with DAG(dag_id="s3_file_transform", default_args=default_args) as dag:
    # [START TASK]
    transformer = S3FileTransformOperator(
        task_id="transform_s3_file",
        source_s3_key=S3_SOURCE_FILE_PATH,
        source_aws_conn_id="aws_localstack",
        dest_s3_key=S3_DEST_FILE_PATH,
        dest_aws_conn_id="aws_localstack",
        transform_script="/opt/airflow/dags/scripts/transform_s3_file.py",
        replace=True,
    )
    # [END TASK]

# [END DAG]

# [START FLOW]
transformer
# [END FLOW]
