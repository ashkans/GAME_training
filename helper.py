from os.path import join, isdir,  basename
from os import makedirs
import os
import numpy as np
from random import seed
from GAME.assignment import Assignment
from glob import glob
import shutil
import sys, yaml
import pandas as pd

def pathModifier(basePath, path):
    if basePath is not None:
        outputPath = join(basePath, path)
        
    else:
        outputPath = path
    
    return outputPath

def dirCheck(path):
    if not isdir(path):
        makedirs(path)    
        
def setSeed(sid):
    seed(sid)
    np.random.seed(sid)

def folderNameGenerator(r, suffix='file'):
    fullName = r['Full name']
    identifier =r['Identifier'].split(sep=' ')[1]
    return  f"{fullName}_{identifier}_assignsubmission_{suffix}_"

def findStudentFolder(r, path):
    identifier =r['Identifier'].split(sep=' ')[1]
    pattern =  join(path, f"*_{identifier}_assignsubmission_*_")
    pathList = glob(pattern)
    print(pattern, pathList)
    assert len(pathList) <= 1, f'multiple match have been found for {identifier}'
    if len(pathList) != 0 :
        out = pathList[0]
    else:
        out = None
    return out


def makeMasterFolder(masterPath, studentFolderName, settings, dbPath, sid):
        studentMasterDir = join(masterPath, studentFolderName)
        dirCheck(studentMasterDir)
        os.chdir(studentMasterDir)
        
        # initialize the assignment class
        assignmentNum = settings['assignmentNum']
        assignment = Assignment(dbPath,
                                 settings['questionList'],
                                 name=settings['assignmnetTitle'],
                                 assignment_num=assignmentNum,
                                 studentID=sid)
        
        assignment.compilers = ['pdflatex', 'pdflatex']
    
        # generate the questions
        assignment.generate_question_list()
    
        # save input files (is needed for marking)
        assignment.save_input_files(studentMasterDir)
    
        # save save tex file1
        assignment.make_assignment_pdf(join(studentMasterDir,'Assignment%d_%s.pdf' \
                                            % (assignmentNum, sid)))
    
        # save assignment
        assignment.save(join(studentMasterDir,'Assignment_class.yml'))
        
def makeSubsetDirPath(path, suffix):
    if path[-1] == os.path.sep:
        newPath = path[:-1]
    else:
        newPath = path
        
    base, name = os.path.split(newPath)
    return (join(base, name+'_'+suffix))
        
def makeSubsetDir(masterPath, studentFolderName, sd, bp):
    studentFolderName = basename(studentFolderName)
    studentMasterDir = join(masterPath, studentFolderName)
    
    if sd['enabled']:
        assignmentSubsetPath = makeSubsetDirPath(masterPath, sd['suffix'])
        
        dirCheck(assignmentSubsetPath)
    
    # make subdriectory
    if sd['enabled']: # subsetPath
        for f in sd['filesToBePassed']:
            studentSubsetDir = join(assignmentSubsetPath, studentFolderName)
            
            dirCheck(studentSubsetDir)
            files_to_be_copied = glob(join(studentMasterDir, f))
        
            for f2c in files_to_be_copied:
                dist = join(studentSubsetDir, basename(f2c))

                shutil.copy2(f2c, dist)
        
        # copy static files
        if 'staticFiles' in sd.keys():
            for sf in sd['staticFiles']:
                msf = pathModifier(bp, sf)
                shutil.copy2(msf, studentSubsetDir)            

def initialize(settingsFile):
    with open(settingsFile, 'r') as file:
        settings = yaml.load(file,  Loader=yaml.Loader)

    # make the required path    
    bp = settings['basePath']
    studentIdListPath = pathModifier(bp, settings['studentIDListFile'])
    dbPath = pathModifier(bp, settings['questionDatabaseDirectory'])
    masterPath = pathModifier(bp, settings['assginmentMasterDirectory'])
    resultPath = pathModifier(bp, settings['resultDirectory'])
    dirCheck(masterPath)
    dirCheck(resultPath)
    

    # the questions are using some helper functions which are located in the path of Question_DB, so they should be accessible:
    sys.path.append(dbPath)    
    return studentIdListPath, dbPath, masterPath, settings