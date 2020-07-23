from GAME.assignment import Assignment
from os.path import join
import os, sys, time, yaml, csv
import pandas as pd
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

df = pd.read_csv(settings['studentIDListFile'])


# the questions are using some helper functions which are located in the path of Question_DB, so they should be accessible:
sys.path.append(join(questionDataBase))


# maek sure that the output_dir exists and make the output file name
A_dir = join(outputDirectory,'Assignment_%s' % assignmentNum)

for r in df.index:
    sid = df.loc[r, 'ID number']
    fullName = df.loc[r,'Full name']
    identifier = df.loc[r,'Identifier'].split(sep=' ')[1]
    folderName = fullName + '_' + identifier + '_' + 'assignsubmission' + '_' + 'file_'
    folderName = folderName.replace(' ', '-')
        
    
    
    seed(float(sid)+float(assignmentNum))
    output_path = join(A_dir, folderName)
    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    os.chdir(output_path)
    # initialize the assignment class
    assignment1 = Assignment(questionDataBase, questionList,name=title ,assignment_num=assignmentNum, studentID=sid)
    assignment1.compilers = ['pdflatex', 'pdflatex']

    # generate the questions
    assignment1.generate_question_list()

    # save input files (is needed for marking)
    assignment1.save_input_files(output_path)

    # save save tex file1

    assignment1.make_assignment_pdf(join(output_path,'Assignment%d_%s.pdf'% (assignmentNum, sid)))

    # save assignment
    assignment1.save(join(output_path,'Assignment_class.yml'))

