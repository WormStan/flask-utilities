from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, BigInteger, DateTime
from sqlalchemy import MetaData

from models_controller.db_manager import DB_Manager


ModelBase = declarative_base()


class BS_Test(ModelBase):
    __tablename__ = "bootstrap_test"

    id = Column(BigInteger, primary_key=True)
    string_col = Column(String(length=100), nullable=False)
    bool_col = Column(Boolean)
    content_col = Column(String(length=500))
    datetime_col = Column(String(length=100))

    def __repr__(self):
        return f"ID is: '{self.id}' \nstring_col is: '{self.string_col}'"


dbm = DB_Manager()
engine = dbm.engine
ModelBase.metadata.create_all(engine)
