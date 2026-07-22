"""
This file will be for databse connection logic.
- Read database config from environment variables
- Define a connection method
- Define database initialisation
"""

import mysql.connector

# Docker is hosting a MySQL database - create method to connect:

config = {
  'user': 'root',
  'password': 'example',
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