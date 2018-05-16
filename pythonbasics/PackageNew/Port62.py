
#import os os.getcwd(), to get current directory,os.chdir('..')-change directory to root
#move to new directory mv Port62.py GeneralPurposeCSV62.py PackageNew
'''
import PackageNew.GeneralPurposeCSV62 #we have to explicitly give package name bcoz for import path is still root directory but
def read_cost(filename,*,errortype="warn"):
    return PackageNew.GeneralPurposeCSV62.read_CSV('Cost.csv',[str,str,int,float],errortype="warn")
'''
#but hardcoding package name is not efficient  and also if we want to move files to new package then we have to
# make changes with new package name
#we can handle it using relative import
from . import GeneralPurposeCSV62
def read_cost(filename,*,errortype="warn"):
    return GeneralPurposeCSV62.read_CSV('Cost.csv',[str,str,int,float],errortype="warn")