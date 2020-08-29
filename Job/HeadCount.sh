#!/bin/bash
. ~/.bash_profile
#################################################
#
#  This is the bash script that is being run by 
#  cron and runs DataEngineering-TestingCentOS 
#  
#
#  Change History
#  --------------------------------
#  Luis Fuentes initial
#################################################

cd /ishome/ssg/lf188653/projects/DataEngineering-HeadCount/
/ishome/ssg/lf188653/.conda/envs/testenv/bin/python main.py /ishome/ssg/lf188653/projects/Data/HEADCOUNT/
