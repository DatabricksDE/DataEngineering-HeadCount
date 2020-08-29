# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Luis Fuentes

from __future__ import annotations
from typing import Optional
import cx_Oracle

class OracleConnection():
    """This class returns a Oracle Connection"""

    def __init__(self):
        self.server: str = ""
        self.user_name: str = ""
        self.password: str = ""
        self.db_instance = cx_Oracle.connect(self.user_name, self.password, self.server)

    def sql_to_data(self, sqlText, dict_values: dict) -> list:
        """This method returns a list of tuples for a specific sql passover parameter"""
        result = []
        try:
            cursor = self.db_instance.cursor()
            rows = cursor.execute(sqlText, dict_values).fetchall()
            for row in rows:
                result.append(row)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            return result
    
    def sql_to_data_no_binding(self, sqlText) -> list:
        """This method returns a list of tuples for a specific sql"""
        result = []
        try:
            cursor = self.db_instance.cursor()
            rows = cursor.execute(sqlText).fetchall()
            for row in rows:
                result.append(row)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            return result
    
    def __del__(self):
        self.db_instance.close()
