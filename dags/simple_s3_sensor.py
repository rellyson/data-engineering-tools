from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow import DAG

with DAG(dag_id="simple_s3_sensor") as dag:
    sensor = S3KeySensor(
        task_id="new_s3_file_in_foobar-bucket",
        aws_conn_id="aws_localstack",
        bucket_key="*",
        wildcard_match=True,
        bucket_name="example-bucket",
        poke_interval=120,
    )

sensor
