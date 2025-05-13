FROM python:3.10-slim-buster
USER root

# Create application directory
RUN mkdir -p /app/airflow
WORKDIR /app

# Copy application files
COPY . /app/

# Install dependencies
RUN pip install -r requirements.txt

# Environment variables
ENV AWS_DEFAULT_REGION="us-east-1"
ENV BUCKET_NAME="houseprice12"
ENV PREDICTION_BUCKET_NAME="my-house-datasource"
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN="sqlite:////app/airflow/airflow.db"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True

# Install Airflow
RUN pip install apache-airflow

# Initialize Airflow database
RUN airflow db init

# Create an Airflow admin user
RUN airflow users create -e srinivasaguru301@gmail.com -f aguru -l srinivas -p admin -r Admin -u admin

# Grant execute permission to the start script
RUN chmod +x start.sh

# Update packages
RUN apt update -y

# Set entrypoint and command
ENTRYPOINT [ "/bin/sh" ]
CMD ["start.sh"]