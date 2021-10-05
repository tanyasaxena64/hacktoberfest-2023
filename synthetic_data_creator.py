# Author: Shivang Nagar
# Usecase: You can make use of the the Faker library in conjunction with other libraries to create synthetic records for usage in volumentric testing.


# Import libraries
from faker import Faker
import csv
import math
import hashlib
import datetime
import random
import pandas as pd


# Instantiating the hashing method and faker obj
hash = haslib.md5()
faker = Faker()


# Data prepreation sample - e.g. customer file:

with open("example-customer.csv", mode='w') as g_file:
	csv_writer = csv.writer(g_file, delimiter=",", quoting=csv.QUOTE_NONE)
	# Creating 100 synthetic customer records
	for i in range(0,99):
		# customerid
		cust_id = " ".join(random.choice("12345679ADBCDEF") for i in range(64)).lower()

		# Date of creation
		snap_date = "05/10/2021"

		# customer type
		customer_type = 'Food Consumer'

		# age
		age = faker.pyint(main_value=18, max_value=90, step=1)

		# customer income 
		cust_incm = faker.pyfloat(left_digits=5, right_digits=2, positive=True)

		# gender
		cust_gndr = faker.bothify(test="?", letters="MF")

		# Create the record
		row = [
			cust_id,
			snap_date,
			customer_type,
			age,
			cust_incm,
			cust_gndr
		]


		# Add to csv
		csv_writer.writerow(row)