import os

import pymysql
from threading import Lock

try:
    # TODO: define the database connection
    schema_db = ""
    user_db = os.getenv('graphus_db_user', "")
    pwd_db = os.getenv('graphus_db_pwd', "")
    address = os.getenv('graphus_db_address', "")
    ip = address.split(":")[0]
    port = address.split(":")[1]
except Exception as db_e:
    print(db_e)


class Database:
    def __init__(self):
        self.lock = Lock()
        try:
            self.conn = pymysql.connect(host=ip,
                                        port=port,
                                        user=user_db,
                                        passwd=pwd_db,
                                        db=schema_db,
                                        cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            self.conn = None
            print(e)
