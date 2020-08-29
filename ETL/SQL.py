# -*- coding: utf-8 -*-
# Created by Luis Fuentes

from __future__ import annotations
from typing import Optional

def getSQLQuery() -> str:
    '''
    This function returns the query that will be executed 
    Return: Str
    '''
    query = '''
            SELECT *
            FROM 
            (
              select  
              C.F_RESOURCE_ID As ID,
              C.F_RESOURCE_NAME As NAME,
              C.F_RESOURCE_TITLE As TITLE,
              C.F_RESOURCE_HIRE_DT As "HIRE DATE",
              C.F_RESOURCE_REHIRE_DT As "REHIRE DATE",
              C.F_RESOURCE_SERVICE_DT As "SERVICE DATE",
              C.F_RESOURCE_NET_ID As "NETWORK ID",
              C.F_RESOURCE_DEPT_ID As "COST CENTER ID",
              C.F_RESOURCE_DEPT_DESC As "COST CENTER DESC",
              C.F_RESOURCE_REGION_ID As "REGION ID",
              C.F_RESOURCE_REGION_DESC As "REGION DESC",
              C.F_RESOURCE_AREA_ID As "AREA ID",
              C.F_RESOURCE_AREA_DESC As "AREA DESC",
              C.F_RESOURCE_DISTRICT_ID As "DIST GEO ID",
              C.F_RESOURCE_DISTRICT_DESC As "DIST GEO DESC",
              C.F_RESOURCE_TYPE As "TYPE",
              C.F_RESOURCE_COMP_CLASS As "WAGE TYPE",
              C.F_RESOURCE_TECH_STATUS As STATUS,
              C.F_RESOURCE_HIRE_STATUS As "TECH STATUS",
              C.F_RESOURCE_MGR_ID As "MGR ID",
              C.F_RESOURCE_MGR_NAME As "MGR NAME",
              C.F_RESOURCE_MGR_DEPT_ID As "MGR DEPT",
              C.F_LEVEL_1_NAME As "LEVEL1 NAME",
              C.F_LEVEL_1_DEPT_ID As "LEVEL1 DEPT",
              C.F_LEVEL_2_NAME As VP,
              C.F_LEVEL_2_DEPT_ID As "LEVEL2 DEPT",
              C.F_LEVEL_3_NAME As "VP/DIRECTOR",
              C.F_LEVEL_3_DEPT_ID As "LEVEL3 DEPT",
              C.F_LEVEL_4_NAME As "LEVEL4 NAME",
              C.F_LEVEL_4_DEPT_ID As "LEVEL4 DEPT",
              C.F_LEVEL_5_NAME As "LEVEL5 NAME",
              C.F_LEVEL_5_DEPT_ID As "LEVEL5 DEPT",
              C.F_LEVEL_6_NAME As "LEVEL6 NAME",
              C.F_LEVEL_6_DEPT_ID As "LEVEL6 DEPT",
              C.F_LEVEL_7_NAME As "LEVEL7 NAME",
              C.F_LEVEL_7_DEPT_ID As "LEVEL7 DEPT",
              C.F_LEVEL_8_NAME As "LEVEL8 NAME",
              C.F_LEVEL_8_DEPT_ID As "LEVEL8 DEPT",
              CASE WHEN UPPER(B.DIR_INDIRECT) = 'I' THEN 'Indirect' ELSE 'Direct' END As BILLABLE,
              D.SAL_ADMIN_PLAN As "SAL PLAN CITY",
              CS.S_NAME As "PHYSICAL SITE",
              CA.ZIPCODE As "PHYSICAL ZIP",
              C.F_TECH_SRVC_CITY As "AMDOCS SERVICE CITY",
              case when C.F_TECH_SRVC_CITY IS NOT NULL then F.CITY_TYPE else NULL end as "AMDOC SERVICE CITY TYPE",
              D.HOME_STATE As "HOME STATE",
              B.POSTAL_CODE As "HOME ZIP CODE",
              A.F_RESOURCE_HR_REGION_ID As "HR REGION ID",
              A.F_RESOURCE_HR_REGION_DESC As "HR REGION DESC",
              A.F_RESOURCE_HR_AREA_ID As "HR AREA ID",
              A.F_RESOURCE_HR_AREA_DESC As "HR AREA DESC",
              A.F_RESOURCE_HR_DISTRICT_ID As "HR DIST GEO ID",
              A.F_RESOURCE_HR_DISTRICT_DESC As "HR DIST GEO DESC",
              A.F_RESOURCE_TECH_TYPE As "HR TECH TYPE",
              case when E.f_tech_org = 'Dispatch Tech' then 'TRUE' else 'FALSE' end as "KPI REPORTING",
              A.F_EMPLOYEE_TEAM As TEAM,
              A.F_BUSINESS_UNIT_LEVEL_3 As "BUSINESS LEVEL UNIT 3",
              B.COUNTRY As COUNTRY,
              B.BIRTH_DATE As "BIRTH DATE",
              B.FULL_PART_TIME As "FULL/PART TIME",
              B.REG_TEMP As "REG TEMP",
              B.EMAIL,
              'CC' as "Empl Type"
              from
                ((( ( ( ( ( ( DW.T_DM_HUMAN_RESOURCES C 
                inner join DW.T_DM_HUMAN_RESOURCES A on A.F_RESOURCE_ID = C.F_RESOURCE_ID  ) 
                cross join DW.T_CLAR_SITE CS ) 
                inner join DW.T_CLAR_EMPLOYEE CE on CE.EMPLOYEE_NO = C.F_RESOURCE_ID AND CE.EMP_PHYSICAL_SITE2SITE = CS.OBJID  ) 
                inner join DW.T_CLAR_ADDRESS CA on CS.CUST_PRIMADDR2ADDRESS = CA.OBJID  ) 
                left join DW.T_CMPC_EMPLOYEE B on B.EMPL_ID = C.F_RESOURCE_ID  )  
                left join DW.EMPLOYEE_HEADER D on D.EMPL_ID = C.F_RESOURCE_ID  )
                inner join  DW.T_DIM_SVC_EMPLOYEE  E  on   A.F_RESOURCE_ID = E.F_TECH_EMPL_ID)
                inner join  DW.T_DIM_SVC_CITY F    on   E.F_TECH_SVC_CITY_SK = F.SVC_CITY_SK)
              where
                C.F_RESOURCE_TECH_STATUS = 'Active'
                and C.F_LEVEL_1_NAME = 'Slattery, Mick'
              
              UNION 

              select
              F.WORKER_KEY As ID,
              A.F_RESOURCE_NAME As NAME,
              FW.TITLE_DESC As TITLE,
              FW.ORIG_START_DATE As "HIRE DATE",
              A.F_RESOURCE_REHIRE_DT As "REHIRE DATE",
              A.F_RESOURCE_SERVICE_DT As "SERVICE DATE",
              A.F_RESOURCE_NET_ID As "NETWORK ID",
              A.F_RESOURCE_DEPT_ID As "COST CENTER ID",
              A.F_RESOURCE_DEPT_DESC As "COST CENTER DESC",
              A.F_RESOURCE_REGION_ID As "REGION ID",
              A.F_RESOURCE_REGION_DESC As "REGION DESC",
              A.F_RESOURCE_AREA_ID As "AREA ID",
              A.F_RESOURCE_AREA_DESC As "AREA DESC",
              A.F_RESOURCE_DISTRICT_ID As "DIST GEO ID",
              A.F_RESOURCE_DISTRICT_DESC As "DIST GEO DESC",
              A.F_RESOURCE_TYPE As "TYPE",
              A.F_RESOURCE_COMP_CLASS As "WAGE TYPE",
              'OPEN' as STATUS,
              A.F_RESOURCE_TECH_STATUS As "TECH STATUS",
              A.F_RESOURCE_MGR_ID As "MGR ID",
              A.F_RESOURCE_MGR_NAME As "MGR NAME",
              A.F_RESOURCE_MGR_DEPT_ID As "MGR DEPT",
              A.F_LEVEL_1_NAME As "LEVEL1 NAME",
              A.F_LEVEL_1_DEPT_ID As "LEVEL1 DEPT",
              A.F_LEVEL_2_NAME As VP,
              A.F_LEVEL_2_DEPT_ID As "LEVEL2 DEPT",
              A.F_LEVEL_3_NAME As "VP/DIRECTOR",
              A.F_LEVEL_3_DEPT_ID As "LEVEL3 DEPT",
              A.F_LEVEL_4_NAME As "LEVEL4 NAME",
              A.F_LEVEL_4_DEPT_ID As "LEVEL4 DEPT",
              A.F_LEVEL_5_NAME As "LEVEL5 NAME",
              A.F_LEVEL_5_DEPT_ID As "LEVEL5 DEPT",
              A.F_LEVEL_6_NAME As "LEVEL6 NAME",
              A.F_LEVEL_6_DEPT_ID As "LEVEL6 DEPT",
              A.F_LEVEL_7_NAME As "LEVEL7 NAME",
              A.F_LEVEL_7_DEPT_ID As "LEVEL7 DEPT",
              A.F_LEVEL_8_NAME As "LEVEL8 NAME",
              A.F_LEVEL_8_DEPT_ID As "LEVEL8 DEPT",
              'FieldGlass' As "BILLABLE",  
              D.SAL_ADMIN_PLAN As "SAL PLAN CITY",
              NULL As "PHYSICAL SITE",
              NULL As "PHYSICAL ZIP",
              A.F_TECH_SRVC_CITY As "AMDOCS SERVICE CITY",
              case when A.F_TECH_SRVC_CITY IS NOT NULL then F.CITY_TYPE else NULL end as "AMDOC SERVICE CITY TYPE",
              FW.STATE_ID As "HOME STATE",
              B.POSTAL_CODE As "HOME ZIP CODE",
              FW.SRVC_REGION As "HR REGION ID",
              FW.SRVC_REGION_NAME As "HR REGION DESC",
              FW.SRVC_AREA As "HR AREA ID",
              FW.SRVC_AREA_NAME As "HR AREA DESC",
              FW.GEO_CODE As "HR DIST GEO ID",
              FW.GEO_DESC As "HR DIST GEO DESC",
              A.F_RESOURCE_TECH_TYPE As "HR TECH TYPE",
              case when E.f_tech_org = 'Dispatch Tech' then 'TRUE' else 'FALSE' end as "KPI REPORTING",
              A.F_EMPLOYEE_TEAM As TEAM,
              A.F_BUSINESS_UNIT_LEVEL_3 As "BUSINESS LEVEL UNIT 3",
              case when FW.COUNTRY_ID = 'CANADA' then 'CAN' else FW.COUNTRY_ID end as COUNTRY,
              B.BIRTH_DATE As "BIRTH DATE",
              B.FULL_PART_TIME As "FULL/PART TIME",
              B.REG_TEMP As "REG TEMP",
              G.E_MAIL,
              'FG with HR' as "Empl Type"
              from
              (select DISTINCT W.COMPUCOM_USER_ID,
                                W.WORKER_KEY,
                                W.MANAGER_ID
                            from dw.t_fg_worker_timesheet FG
                            inner join  dw.t_fg_worker W          on W.WORKER_KEY = fg.FIELDGLASS_ID
                            where TIME_ENTRY_DT >= TRUNC(sysdate, 'DAY') - (8)
                            and TIME_ENTRY_DT <= TRUNC(sysdate, 'DAY') - (2))F 
                inner join dw.t_fg_worker FW on FW.WORKER_KEY = F.WORKER_KEY  
                inner join DW.T_DM_HUMAN_RESOURCES A on A.F_RESOURCE_ID = F.COMPUCOM_USER_ID
                left join  DW.T_CMPC_EMPLOYEE B on B.EMPL_ID = A.F_RESOURCE_ID   
                left join  DW.EMPLOYEE_HEADER D on D.EMPL_ID = A.F_RESOURCE_ID 
                left join  DW.T_DIM_SVC_EMPLOYEE  E  on   A.F_RESOURCE_ID = E.F_TECH_EMPL_ID
                left join  DW.T_DIM_SVC_CITY F    on   E.F_TECH_SVC_CITY_SK = F.SVC_CITY_SK
                left join  T_CLAR_EMPLOYEE G    ON  A.f_resource_id = G.s_employee_no 
              where A.F_LEVEL_1_NAME = 'Slattery, Mick'

              UNION

              select
              F.WORKER_KEY As ID ,
              FW.RESOURCE_NAME As NAME,
              FW.TITLE_DESC As TITLE,
              FW.ORIG_START_DATE As "HIRE DATE",
              A.F_RESOURCE_REHIRE_DT As "REHIRE DATE",
              A.F_RESOURCE_SERVICE_DT As "SERVICE DATE",
              FW.COMPUCOM_USER_ID As "NETWORK ID",
              FW.DEPARTMENT_ID As "COST CENTER ID",
              FW.DEPARTMENT_DESC As "COST CENTER DESC",
              FW.SRVC_REGION As "REGION ID",
              FW.SRVC_REGION_NAME As "REGION NAME",
              FW.SRVC_AREA As "AREA ID",
              FW.SRVC_AREA_NAME As "AREA NAME",
              FW.GEO_CODE As "DIST GEO ID",
              FW.GEO_DESC As "DIST GEO DESC",
              A.F_RESOURCE_TYPE As "TYPE",
              A.F_RESOURCE_COMP_CLASS As "WAGE TYPE",
              'OPEN' as STATUS,
              A.F_RESOURCE_HIRE_STATUS As "TECH STATUS",
              FW.MANAGER_ID As "MGR ID",
              FW.MANAGER_NAME As "MGR NAME",
              C.F_RESOURCE_DEPT_ID As "MGR DEPT",
              C.F_LEVEL_1_NAME As "LEVEL1 NAME",
              C.F_LEVEL_1_DEPT_ID As "LEVEL1 DEPT",
              C.F_LEVEL_2_NAME As VP,
              C.F_LEVEL_2_DEPT_ID As "LEVEL2 DEPT",
              C.F_LEVEL_3_NAME As "VP/DIRECTOR",
              C.F_LEVEL_3_DEPT_ID As "LEVEL3 DEPT",
              C.F_LEVEL_4_NAME As "LEVEL4 NAME",
              C.F_LEVEL_4_DEPT_ID As "LEVEL4 DEPT",
              C.F_LEVEL_5_NAME As "LEVEL5 NAME",
              C.F_LEVEL_5_DEPT_ID As "LEVEL5 DEPT",
              C.F_LEVEL_6_NAME As "LEVEL6 NAME",
              C.F_LEVEL_6_DEPT_ID As "LEVEL6 DEPT",
              C.F_LEVEL_7_NAME As "LEVEL7 NAME",
              C.F_LEVEL_7_DEPT_ID As "LEVEL7 DEPT",
              C.F_LEVEL_8_NAME As "LEVEL8 NAME",
              C.F_LEVEL_8_DEPT_ID As "LEVEL8 DEPT",
              'FieldGlass' As "BILLABLE",
              D.SAL_ADMIN_PLAN As "SAL PLAN CITY",
              NULL As "PHYSICAL SITE",
              NULL As "PHYSICAL ZIP",
              A.F_TECH_SRVC_CITY As "AMDOCS SERVICE CITY",
              case when A.F_TECH_SRVC_CITY IS NOT NULL then F.CITY_TYPE else NULL end as "AMDOC SERVICE CITY TYPE",-----check
              FW.STATE_ID As "HOME STATE",
              B.POSTAL_CODE As "HOME ZIP CODE",
              FW.SRVC_REGION As "HR REGION",
              FW.SRVC_REGION_NAME As "HR REGION DESC",
              FW.SRVC_AREA As "HR AREA",
              FW.SRVC_AREA_NAME As "HR AREA DESC",
              FW.GEO_CODE As "HR DISTRICT",
              FW.GEO_DESC As "HR DISTRICT DESC",
              A.F_RESOURCE_TECH_TYPE As "HR TECH TYPE",
              case when E.f_tech_org = 'Dispatch Tech' then 'TRUE' else 'FALSE' end as "KPI REPORTING",
              A.F_EMPLOYEE_TEAM As TEAM,
              A.F_BUSINESS_UNIT_LEVEL_3 As "BUSINESS LEVEL UNIT 3",
              case when FW.COUNTRY_ID = 'CANADA' then 'CAN' else FW.COUNTRY_ID end as COUNTRY,
              B.BIRTH_DATE As "BIRTH DATE",
              B.FULL_PART_TIME As "FULL/PART TIME",
              B.REG_TEMP As "REG TEMP",
              FW.WORKER_EMAIL,
              'FG no HR' as "Empl Type" 
              from
              (select DISTINCT W.COMPUCOM_USER_ID,
                              W.WORKER_KEY,
                              W.MANAGER_ID
                            from dw.t_fg_worker_timesheet FG
                            inner join  dw.t_fg_worker W          on W.WORKER_KEY = fg.FIELDGLASS_ID
                            where TIME_ENTRY_DT >= TRUNC(sysdate, 'DAY') - (8)
                            and TIME_ENTRY_DT <= TRUNC(sysdate, 'DAY') - (2)) F 
                            
                inner join dw.t_fg_worker FW on FW.WORKER_KEY = F.WORKER_KEY
                left join DW.T_DM_HUMAN_RESOURCES A on A.F_RESOURCE_ID = F.COMPUCOM_USER_ID 
                left join DW.T_DM_HUMAN_RESOURCES C on C.F_RESOURCE_ID = F.MANAGER_ID 
                left join DW.T_CMPC_EMPLOYEE B on B.EMPL_ID = A.F_RESOURCE_ID   
                left join DW.EMPLOYEE_HEADER D on D.EMPL_ID = A.F_RESOURCE_ID
                left join  DW.T_DIM_SVC_EMPLOYEE  E  on   A.F_RESOURCE_ID = E.F_TECH_EMPL_ID
                left join  DW.T_DIM_SVC_CITY F    on   E.F_TECH_SVC_CITY_SK = F.SVC_CITY_SK 
              where A.F_RESOURCE_NET_ID Is null
              and C.F_LEVEL_1_NAME = 'Slattery, Mick'
            )
            '''
    return query