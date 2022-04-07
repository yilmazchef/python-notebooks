from dotenv import load_dotenv

load_dotenv()

import os
import MySQLdb

try:

    connection = MySQLdb.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USERNAME"),
        passwd=os.getenv("PASSWORD"),
        db=os.getenv("DATABASE")
    )
    
except MySQLdb._exceptions.OperationalError as err:
    print(err)
    

