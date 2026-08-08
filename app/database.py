"""
This file will be used for database connection logic.
- Read database config from environment variables
- Define a connection method
- Define database initialisation
"""

import mysql.connector
import os


# Until I create a python app container use local txt file for accessing db (once this app is containerised use the secret):
BASE_PATH = os.path.dirname(os.path.abspath(__file__))  # Ensures this script can be run from any directory
password_path = os.path.join(BASE_PATH, "..", "secrets", "db_password.txt")

with open(password_path) as password_file:
  password = password_file.read()


# Docker is hosting a MySQL database - create method to connect:
config = {
  'user': 'root',
  'password': password,
  'host': '127.0.0.1',  # Temporarily use localhost, when containerised use the service name 'db' (Docker has a built-in DNS server)
  'port': 3306,
  'database': 'user_details',  # Tells MySQL to create a database (schema) with this name
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()

print("Completed successfully")

"""
Finding docker IP address:
docker inspect \
  -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id>
"""