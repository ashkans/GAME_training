from GAME.assignment import Assignment
from os.path import join, basename, dirname
import os, sys, time, yaml, csv
import pandas as pd
from random import seed
from glob import glob
import shutil



settingsFile = sys.argv[1]

with open(settingsFile, 'r') as file:
    settings = yaml.load(file)
    
    
outputDirectory = settings['outputDirectory']
assignmentNum = settings['assignmentNum']
filesToCopy = settings['filesToBePassedToStudents']

#outputDirectory = '/home/ashkans/git/GAME_output'


toMoodleDir = join(outputDirectory,'Assignment_%s_to_moodle' % assignmentNum)
A_dir = join(outputDirectory,'Assignment_%s' % assignmentNum)


if not os.path.isdir(toMoodleDir):    
    os.makedirs(toMoodleDir)


studentDirList = glob(join(A_dir, '*'))

for student_dir in studentDirList:
    for f in filesToCopy:
        student_dir_basename = dirname(student_dir)
        new_student_dir_basename = basename(student_dir)#.replace('-', ' ')
        
        new_student_dir = join(toMoodleDir, new_student_dir_basename)
        
        if not os.path.isdir(new_student_dir):    
            os.makedirs(new_student_dir)   
            
        files_to_be_copied = glob(join(student_dir, f))
        
        for f2c in files_to_be_copied:
            dist = join(new_student_dir, basename(f2c))
            shutil.copy2(f2c, dist)
        
        # copy static files
         
        if 'staticFiles' in settings.keys():
            for sf in settings['staticFiles']:
                shutil.copy2(sf, new_student_dir)
                
        



        
    