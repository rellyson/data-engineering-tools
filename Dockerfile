FROM apache/airflow:2.8.1

# install necessary packages
RUN pip install apache-airflow-providers-amazon pandas plotly

# migrate database
RUN airflow db init

# add airflow user
RUN airflow users create --user airflow \
    -f Airflow \
    -l User \
    -p airflow \
    -r Admin \
    -e foo@airflow.com

# create localstack custom connection
RUN airflow connections add 'aws_localstack' \
    --conn-json '{"conn_type":"aws","login":"foobar","password":"foobar","extra":{"endpoint_url":"http://localstack:4566/","region_name":"us-east-1"}}'
