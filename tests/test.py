import unittest
import logging
import pymysql
import os
import sys

sys.path.append(os.getcwd())
from quickutil4py import file_util
from quickutil4py import datetime_util
from quickutil4py import db_util

db_config = {'host': 'xx.xx.xx.xx', 'port': 3306, 'user': 'xxx', 'password': 'xxxx', 'database': 'xxxx', 'charset': 'utf8mb4'}


class TestUtil(unittest.TestCase):

    def test_file_util():
        logging.info(file_util.get_current_path())

    def test_datetime():
        logging.info(datetime_util.timestamp_2_date(1672502400))
        logging.info(datetime_util.date_2_timestamp("2023-01-05"))

    def test_db_insert_list():
        db_util.add_db("test", pymysql, db_config)
        id = 0
        list = []
        while id < 10:
            id += 1
            list.append({"id": id, "name": "try"})
        db_util.insert_list("test", "test", list)

    def test_db_select():
        db_util.add_db("test", pymysql, db_config)
        results = db_util.select("test", "select * from test limit 10")
        logging.info(results)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)
    TestUtil.test_datetime()
