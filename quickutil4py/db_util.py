import logging
from dbutils.pooled_db import PooledDB
from collections.abc import Iterable


db_map = {str: PooledDB}


def add_db(db_name: str, db_driver, db_config:map, mincached=0, maxcached=0,
           maxshared=0, maxconnections=0, blocking=False,
           maxusage=None, setsession=None, reset=True,
           failures=None, ping=1):
    if db_name in db_map.keys():
        logging.error("DB "+db_name + " already exists")
        return
    db_map[db_name] = PooledDB(db_driver, mincached, maxcached,
                               maxshared, maxconnections, blocking,
                               maxusage, setsession, reset,
                               failures, ping, **db_config)


def remove_db(db_name: str):
    if db_map[db_name] != None:
        logging.warn("DB "+db_name + " not exists")
        return
    db_map[db_name].close()
    db_map[db_name] = None


def select(db_name: str, sql: str):
    conn = db_map[db_name].connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def execute(db_name: str, sql: str, **params):
    conn = db_map[db_name].connection()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()
    return True


def insert_list(db_name: str, table_name: str, lines: Iterable[map]):
    if len(lines) == 0:
        return True
    if len(lines[0]) == 0:
        return True
    if len(lines) > 1000:
        logging.error("max line number is 1000")
        return False
    # 组装参数模版
    param_tmpl = "("
    for key in lines[0]:
        param_tmpl += "%s,"
    param_tmpl = param_tmpl[0:len(param_tmpl)-1]+")"
    # 拼接参数模版
    params = []
    sql = "insert into "+table_name+" ("
    for key in lines[0]:
        sql += key+","
    sql = sql[0:len(sql)-1]+") values"
    for line in lines:
        sql += param_tmpl+","
        for key in lines[0]:
            params.append(line[key])
    sql = sql[0:len(sql)-1]
    # 拼接参数
    logging.info(sql)
    logging.info(params)
    conn = db_map[db_name].connection()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()
    return True
