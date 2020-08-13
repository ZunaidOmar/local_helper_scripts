import sys
import os
import subprocess
import pandas as pd


def Host_Name_Ping(host_path_file):

     #empty arrays which we will convert to dictionaries later

     successful = []
     unsuccessful =[]

     scriptDir = sys.path[0]
     hosts = os.path.join(scriptDir,host_path_file)
     hostsFile = open(hosts,"r")

     lines = hostsFile.readlines()

     for line in lines:
         line = line.strip(' ')
         line = line.strip('\n')
         line = line.strip('\t')
         line = line.strip(' ,')


         param = '-n'

         command = ['ping',param,'3',line]

         if subprocess.call(command)==0:
             successful.append(line)
         else:
             unsuccessful.append(line)


         my_dict = {'Successful':successful,'Unsuccessful':unsuccessful}
         with open('test.csv','w')as f:
             for key in my_dict.keys():
                f.write("%s,%s\n"%(key,my_dict[key]))


Host_Name_Ping("C:\\Users\\T440P\\Documents\\Hosts.txt")               