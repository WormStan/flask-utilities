import traceback

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from log import log

from models_controller import config as config

logger = log.setup_custom_logger('db_manager')


class DB_Manager():
    def __init__(self):
        _host = config.HOST
        _port = config.PORT
        _user = config.USER
        _passwd = config.PWD
        _db = config.DATABASE
        self.engine = create_engine(f"mysql+pymysql://{_user}:{_passwd}@{_host}:{_port}/{_db}", echo=False)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def add_row(self, obj):
        try:
            self.session.add(obj)
            self.session.commit()
            return obj
        except Exception:
            logger.error(str(traceback.format_exc()))
            self.session.rollback()

    def query_first(self, obj, condition):
        try:
            result = self.session.query(obj).filter(condition).first()
        except NoResultFound:
            result = None
        return result

    def query_all(self, obj, condition=None):
        if condition is not None:
            result_list = self.session.query(obj).filter(condition).all()
        else:
            result_list = self.session.query(obj).all()
        return result_list

    def update_by_filter(self, obj, update_hash, condition):
        try:
            self.session.query(obj).filter(condition).update(update_hash)
            self.session.commit()
        except Exception:
            logger.error(str(traceback.format_exc()))
            self.session.rollback()

    def delete_by_filter(self, obj, condition):
        try:
            self.session.query(obj).filter(condition).delete()
            self.session.commit()
        except Exception:
            logger.error(str(traceback.format_exc()))
            self.session.rollback()

    def execute_sql_query(self,sql_str):
        return self.session.execute(sql_str).fetchall()