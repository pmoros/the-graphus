"""Handle database configuration."""
import os
from threading import Lock

import pymysql

try:
    schema_db = "the_graphus"
    user_db = os.getenv("the_graphus_db_user", "")
    pwd_db = os.getenv("the_graphus_db_pwd", "")
    address = os.getenv("the_graphus_db_address", "")
    ip = address.split(":")[0]
    port = int(address.split(":")[1])

except Exception as db_e:
    print(db_e)


class Database:
    def __init__(self):
        self.lock = Lock()
        try:
            self.conn = pymysql.connect(
                host=ip,
                port=port,
                user=user_db,
                passwd=pwd_db,
                db=schema_db,
                cursorclass=pymysql.cursors.DictCursor,
            )
        except Exception as e:
            self.conn = None
            print(e)
