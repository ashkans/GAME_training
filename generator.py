#!/usr/bin/env python
# coding: utf-8

# In[15]:


# import modules
from GAME.assignment import Assignment
from os.path import join
import os, sys, time, yaml, csv
from random import seed


settingsFile = sys.argv[1]
#settingsFile = r'settings/settings.yaml'


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

questionList = settings['questionList']

with open(settings['studentIDListFile']) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    studentIDList = [r[0] for r in readCSV]


# the questions are using some helper functions which are located in the path of Question_DB, so they should be accessible:
sys.path.append(join(questionDataBase))


# maek sure that the output_dir exists and make the output file name
A_dir = join(outputDirectory,'Assignment_%s' % assignmentNum)

for sid in studentIDList:
    seed(float(sid)+float(assignmentNum))
    output_path = join(A_dir, 'A%d_%s' % (assignmentNum, sid))
    if not os.path.isdir(output_path):
        os.makedirs(output_path)


    # initialize the assignment class
    assignment1 = Assignment(questionDataBase, questionList,name=title ,assignment_num=assignmentNum, studentID=sid)

    # generate the questions
    assignment1.generate_question_list()

    # save input files (is needed for marking)
    assignment1.save_input_files(output_path)

    # save save tex file1
    assignment1.make_assignment_pdf(join(output_path,'Assignment%d_%s.pdf'% (assignmentNum, sid)))

    # save assignment
    assignment1.save(join(output_path,'Assignment_class.yml'))

