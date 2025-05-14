FROM python:3.10-slim-buster

# Set the user to root
USER root

# Create the application directory
RUN mkdir /app

# Copy the application code
COPY . /app/
WORKDIR /app/

# Install necessary packages for Airflow
RUN pip3 install --no-cache-dir -r requirements.txt

# Update environment variables
ENV AWS_DEFAULT_REGION="us-east-1"
ENV BUCKET_NAME="houseprice12"
ENV PREDICTION_BUCKET_NAME="my-house-datasource"
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True
RUN airflow db init
RUN airflow users create -e srinivasaguru301@gmail.com -f aguru -l srinivas -p admin -r Admin -u admin
# Set permissions for the start script
RUN chmod 777 start.sh
RUN apt update -y
# Airflow entry point
ENTRYPOINT ["/bin/sh"]
CMD ["start.sh"]
