import random
import string
import time

from sqlalchemy import and_

from log import log
from models.models import BS_Test as bs_test
from models_controller.db_manager import DB_Manager

logger = log.setup_custom_logger('common_controller')


class Common_Controller:

    def __init__(self):
        self.dbm = DB_Manager()

    def bs_get_all(self):
        condition = (bs_test.id < 500)
        rows = self.dbm.query_all(
            obj=bs_test, condition=condition
        )
        return rows

    def bs_add_row(self):
        datetime_value = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        string_value = username_suffix = ''.join(random.sample(
            string.ascii_letters + string.digits, 4))

        bs_row = bs_test(string_col=string_value, bool_col=1,
                         content_col='Bootstrap Table Col Content', datetime_col=datetime_value)
        if self.dbm.add_row(bs_row):
            return True
        else:
            return False