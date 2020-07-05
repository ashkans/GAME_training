#!/usr/bin/env python
# coding: utf-8

import sys
from GAME.assignment import  load_assignment
from os.path import join
import csv
import pandas as pd
from GAME.fileNameManager import FileNameManager
import yaml


settingsFile = sys.argv[1]
#settingsFile = r'training_data/settings.yaml'


with open(settingsFile, 'r') as file:
    settings = yaml.load(file)
    
# setting the path of question data base
questionDataBase = settings['questionDataBase']
# seetin the path for the outputs (question pdf)
outputDirectory = settings['outputDirectory']
# the assignment number, to be shown in the pdfs
assignmentNum = settings['assignmentNum']
# name 
title = settings['assignmnetTitle']

with open(settings['studentIDListFile']) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    studentIDList = [r[0] for r in readCSV]


# the questions are using some helper functions which are located in the path of Question_DB, so they should be accessible:
sys.path.append(join(questionDataBase))


A_dir = join(outputDirectory,'Assignment_%s' % assignmentNum)

for studentID in studentIDList:
    output_path = join(A_dir, 'A%d_%s' % (assignmentNum, studentID))
    #load assignment
    print(join(output_path, 'Assignment_class.yml'))
    
    assignment = load_assignment(join(output_path, 'Assignment_class.yml'))

    # results path
    resutls_path = []

    # load the inputs
    for q in assignment.questions:
        fnm = FileNameManager(studentID, assignmentNum, q.qid)
        q.text.inputs = q.marking.input_loader(join(output_path,fnm.getInputFileName()))
        resutls_path.append(join(output_path,fnm.getAnswerFileName()))

    # get feedback and mark
    assignment.mark_and_get_feedbacks(resutls_path)

    # write the feedback file
    assignment.make_feedback_pdf(join(output_path,fnm.feedbackFileName()), name=title ,assignment_num=assignmentNum-1)

