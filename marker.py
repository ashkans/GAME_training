#!/usr/bin/env python
# coding: utf-8

import sys, os
from GAME.assignment import  load_assignment
from os.path import join
import csv
import pandas as pd
from GAME.fileNameManager import FileNameManager
import yaml
from glob import glob

settingsFile = sys.argv[1]
#settingsFile = r'training_data/settings.yaml'


with open(settingsFile, 'r') as file:
    settings = yaml.load(file)
    
# setting the path of question data base
questionDataBase = settings['questionDataBase']
# seetin the path for the outputs (question pdf)
outputDirectory = settings['outputDirectory']
studentResultsFolder = settings['studentResultsFolder']
# the assignment number, to be shown in the pdfs
assignmentNum = settings['assignmentNum']
# name 
title = settings['assignmnetTitle']
        
df = pd.read_csv(settings['studentIDListFile'])

    
# the questions are using some helper functions which are located in the path of Question_DB, so they should be accessible:
sys.path.append(join(questionDataBase))


A_dir = join(outputDirectory,'Assignment_%s' % assignmentNum)

markList = pd.DataFrame(columns=['mark', 'letter mark', 'full name'])

for r in df.index:
    sid = df.loc[r, 'ID number']
    fullName = df.loc[r,'Full name']
    identifier = df.loc[r,'Identifier'].split(sep=' ')[1]
    #folderName = fullName + '_' + identifier + '_' + 'assignsubmission' + '_' + 'file_'
    #folderName = folderName.replace(' ', '-')
    output_path_pattern = join(A_dir, '*_' + identifier + '_' + 'assignsubmission' + '_' + 'file_')
    output_folderName = os.path.basename(glob(output_path_pattern)[0])
    
    output_path_pattern = join(studentResultsFolder, '*_' + identifier + '_' + 'assignsubmission' + '_' + 'file_')
    outoutList = glob(output_path_pattern)
    if len(outoutList) != 0:
        studentResultsFolder_folderName = os.path.basename(outoutList[0])
        
        output_path = join(A_dir, output_folderName)
        result_path = join(studentResultsFolder, studentResultsFolder_folderName)
        #load assignment
        print(join(output_path, 'Assignment_class.yml'))
        
        assignment = load_assignment(join(output_path, 'Assignment_class.yml'))
    
        # results path
        resutls_path = []
    
        # load the inputs
        for q in assignment.questions:
            fnm = FileNameManager(sid, assignmentNum, q.qid)
            q.text.inputs = q.marking.input_loader(join(output_path,fnm.getInputFileName()))
            resutls_path.append(join(result_path,fnm.getAnswerFileName()))
    
        # get feedback and mark
        assignment.mark_and_get_feedbacks(resutls_path)
    
        # write the feedback file
        feedbackPath = result_path
        if not os.path.isdir(feedbackPath):
            os.makedirs(feedbackPath)    
        assignment.make_feedback_pdf(join(feedbackPath,fnm.feedbackFileName()), name=title ,assignment_num=assignmentNum)
        
        markList.loc[sid, 'full name'] = fullName
        markList.loc[sid, 'mark'] = assignment.mark
        markList.loc[sid, 'letter mark'] = assignment.letterMark

if 'marksOutputPath' in settings.keys():
    markList.to_csv(settings['marksOutputPath'])
else:
    markList.to_csv('marks.csv')