!bin/sh

echo "Starting Airflow webserver and scheduler..."
airflow webserver --port 8080 & 
airflow scheduler