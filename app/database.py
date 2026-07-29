"""
This file will be for databse connection logic.
- Read database config from environment variables
- Define a connection method
- Define database initialisation
"""

import mysql.connector


# Until I create a python app container use local txt file for accessing db:
with open("../secrets/db_password.txt") as password_file:
  password = password_file.read()


# Docker is hosting a MySQL database - create method to connect:
config = {
  'user': 'root',
  'password': password,
  'host': '172.18.0.2',
  'database': 'employees',  # what to insert here if db not yet created?
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