from functools import wraps
import pymysql

from app.log import logger


def with_connection(f):
    @wraps(f)
    def with_connection_(self, *args, **kwargs):
        try:
            self.conn.ping()
            result = f(self, *args, **kwargs)
        except pymysql.IntegrityError as e:
            raise e
        except Exception as e:
            self.conn.rollback()
            logger.exception("Unable to operate on database. %s", e)
        else:
            self.conn.commit()
        finally:
            self.conn.close()

        return result

    return with_connection_
