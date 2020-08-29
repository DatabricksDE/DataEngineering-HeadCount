# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Luis Fuentes

from __future__ import annotations
from typing import Optional
from pathlib import Path
from ETL.GeneralFunctions import (
    move_master_file, getMasterFilePath, append_df_to_excel,
    getDates, upload_to_bucket, delete_processed_file,
    getFilesDirectoryPath
)
from ETL.SQL import getSQLQuery
from ETL.DBConn import OracleConnection
import logging
import sys
import os
import pandas as pd
import numpy as np

if __name__ == "__main__":

    try:
        # 0.- Setup the logging object
        LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        loggin_file_path = str(Path('{path}/HeadCount.log'.format(path = os.getcwd())))
        logging.basicConfig(filename = loggin_file_path,
                            level = logging.DEBUG,
                            format = LOG_FORMAT,
                            filemode = 'w')
        
        logger = logging.getLogger()

        # 1.- Getting a copy of the master file in the process directory
        logger.info("Begin copying Master file")
        #files_directory_path = Path(sys.argv[1])
        files_directory_path = getFilesDirectoryPath()
        move_master_file(getMasterFilePath(), files_directory_path)
        logger.info("Done copying Master file")

        # 2.- Connecting to DW
        logger.info("Stablishing connection with DW")
        oracle_conn = OracleConnection()
        logger.info("Running query")
        result = oracle_conn.sql_to_data_no_binding(getSQLQuery())
        logger.info("Done running query")

        # 3.- Ceaning data
        logger.info("Cleaning Data")
        df = pd.DataFrame(result)
        columns = ["ID","NAME","TITLE","HIRE DATE","REHIRE DATE","SERVICE DATE","NETWORK ID","COST CENTER ID","COST CENTER DESC","REGION ID","REGION DESC","AREA ID","AREA DESC","DIST GEO ID","DIST GEO DESC","TYPE","WAGE TYPE","STATUS","TECH STATUS","MGR ID","MGR NAME","MGR DEPT","LEVEL1 NAME","LEVEL1 DEPT","VP","LEVEL2 DEPT","VP/DIRECTOR","LEVEL3 DEPT","LEVEL4 NAME","LEVEL4 DEPT","LEVEL5 NAME","LEVEL5 DEPT","LEVEL6 NAME","LEVEL6 DEPT","LEVEL7 NAME","LEVEL7 DEPT","LEVEL8 NAME","LEVEL8 DEPT","BILLABLE","SAL PLAN CITY","PHYSICAL SITE","PHYSICAL ZIP","AMDOCS SERVICE CITY","AMDOC SERVICE CITY TYPE","HOME STATE","HOME ZIP CODE","HR REGION ID","HR REGION DESC","HR AREA ID","HR AREA DESC","HR DIST GEO ID","HR DIST GEO DESC","HR TECH TYPE","KPI REPORTING","TEAM","BUSINESS LEVEL UNIT 3","COUNTRY","BIRTH DATE","FULL/PART TIME","REG TEMP","EMAIL","Empl Type"]
        df.set_axis(columns, axis=1, inplace=True)

        # Finding duplicates based on Network ID
        value_counter = df['NETWORK ID'].value_counts()
        duplicates = value_counter[value_counter>1].to_dict()
        
        # Deleting duplicates
        for key in duplicates.keys():
            if len(key) != 0:
                df.drop(df[(df['NETWORK ID'] == key) & (df['Empl Type'] != 'CC')].index , inplace=True)

        # 4.- Copying raw data to 
        logger.info('Copying Data to file')
        final_file_path = Path('{one}/Head_Count.xlsx'.format(one=files_directory_path))
        append_df_to_excel(final_file_path, df, sheet_name='03 Current Details', index=False, header=False)

        # 5.- Send Data to bucket
        logger.info('Copying File to Bucket')
        bucket_file_name = 'appusma206_apps/output/HeadCount/Head_Count_{year}_{month}_{day}.xlsx'.format(year=getDates('getSheetByYear'), month=getDates('getSheetByMonth'), day=getDates('getSheetByDay'))

        upload_to_bucket(final_file_path, bucket_file_name)
        logger.info('File uploaded to appusma206_apps_output')

        # 6.- Deleting local file copy
        logger.info('Deleting temporary file')
        delete_processed_file(final_file_path)

    except Exception as e:
        logger.error(e)
        #print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        sys.exit()
