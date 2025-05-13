FROM python:3.10-slim-buster
USER root
RUN mkdir /app
COPY . /app/
WORKDIR /app/
RUN pip3 install -r requirements.txt
ENV AWS_DEFAULT_REGION="us-east-1"
ENV BUCKET_NAME="houseprice12"
ENV PREDICTION_BUCKET_NAME="my-house-datasource"
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True
RUN airflow db migrate
RUN airflow create_user -r Admin -u admin -p admin -f aguru -l srinivas -e srinivasaguru301@gmail.com
RUN chmod 777 start.sh
RUN apt update -y
ENTRYPOINT [ "/bin/sh" ]
CMD ["start.sh"]