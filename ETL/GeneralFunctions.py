# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Luis Fuentes

from __future__ import annotations
from typing import Optional

def getDates(place_holder:str = 'getSheetByDay'):
    '''
    This function returns a date, it comes in 3 flavors: getSheetByDay, getSheetByMonth, getSheetByYear
    Arg01: place_holder = This will be the string that has to be passed over the funtion, its default value is getSheetByDay
    Return: This will return a number either (Year, month, day)
    '''
    import datetime

    REGISTRY = {
        'getSheetByDay': datetime.date.today().day,
        'getSheetByMonth': datetime.date.today().month,
        'getSheetByYear': datetime.date.today().year
    }

    return REGISTRY[place_holder]

def upload_to_bucket(file_name, object_name:str):
    '''
    Upload a file to the cloud, this method does not return anything. Decorator for AWS
    :param file_name: File to upload
    :param object_name: Path/Name of the file that will be placed in bucket.
    '''
    from google.cloud import storage
    from google.oauth2 import service_account
    from pathlib import Path
    from os.path import basename
    import os

    # Reading credentials
    credentials_path = Path('') # Add the creds here: # C:\\Users\\lf188653\\GCPKey\\microstrategyit-749574041a8c.json
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(credentials_path)
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    
    dictionary = {'bucketName': 'appusma206_apps_output',
                  'destination_blob_name': 'appusma206_apps/HeadCount/{year}/{month}/{day}/{name}'.format(year=getDates('getSheetByYear'), month=getDates('getSheetByMonth'), day=getDates('getSheetByDay'), name=basename(object_name)),
                  'source_file_name': f'{file_name}'}

    storage_client = storage.Client(credentials=credentials)

    storage_client.get_bucket(dictionary['bucketName']).blob(dictionary['destination_blob_name'])\
        .upload_from_filename(dictionary['source_file_name'])

def delete_processed_file(file_final_path:str) -> None:
    '''
    Deletes a file
    Arg01: file_final_path: This is the string of the full path on which the file is placed  
    Return: None
    '''
    import os

    os.remove(file_final_path)

def move_master_file(file_path_ext, file_path_destination) -> None:
    '''
    This function moves the Master file to a working directory.
    Arg01: file_path_ext: This is the file path of the Master file including file extension
    Arg02: file_path_destination: This is the file path where the file will be copy, with out the extension.
    Return: None
    '''
    from shutil import copy2
    
    copy2(file_path_ext, file_path_destination)

def getMasterFilePath() -> object:
    '''
    This function returns the location of the Master file, this is included under the Masterfile folder under this repo
    Args: None
    '''
    import os
    from pathlib import Path
    
    return Path('{path}/MasterFile/Head_Count.xlsx'.format(path = os.getcwd()))

def getFilesDirectoryPath()-> object:
    """Returns the pathlib Path for the output file

    Returns:
        object: pathlib Path
    """
    import os
    from pathlib import Path
    return Path(os.getcwd(),'output')

def append_df_to_excel(file_path, df, start_row=1, sheet_name='Sheet1', index=False, header=False) -> None:
    '''
    This function writes a pandas Data Frame to an existing Excel File
    Args01: file_path: This is the full path of the file on which the data will be posted
    Args02: df: this is the pandas Data Frame.
    Args03: start_row: This is an optional parameter for the row on whitch it will start writting. Default is set up at the second row
    Args04: sheet_name: This is the sheet on which the data frame will be placed
    Args05: index: These are the index True or False must be placed otherwise False is the default value.
    Args06: header: These are the headers of the dataframe
    Return: None
    '''
    import sys
    import pandas as pd
    from pandas import ExcelWriter
    from openpyxl import load_workbook
    
    try:    
        #Open existing excel file
        workbook1 = load_workbook(file_path, read_only=False)

        writer = pd.ExcelWriter(file_path, engine='openpyxl')
        writer.book = workbook1
        writer.sheets = dict((ws.title, ws) for ws in workbook1.worksheets)
        # Add dataframe to excel file 
        # df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=start_row, startcol=1)
        df.to_excel(writer, index=index, startrow=start_row, startcol=0, header=header, sheet_name=sheet_name)
    except Exception as e:
        print(e)
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    finally:        
        writer.save()
        writer.close()

