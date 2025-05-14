FROM python:3.10-slim-buster

# Set the user to root
USER root

# Create the application directory
RUN mkdir /app

# Copy the application code
COPY . /app/
WORKDIR /app/

# Install necessary packages for Airflow
RUN apt-get update -y && \
    apt-get install -y build-essential libssl-dev libffi-dev python3-dev && \
    pip3 install --no-cache-dir -r requirements.txt

# Update environment variables
ENV AWS_DEFAULT_REGION="us-east-1"
ENV BUCKET_NAME="houseprice12"
ENV PREDICTION_BUCKET_NAME="my-house-datasource"
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True

# Set permissions for the start script
RUN chmod +x start.sh

# Initialize the Airflow database
RUN airflow initdb

# Airflow entry point
ENTRYPOINT ["airflow"]
CMD ["standalone"]
