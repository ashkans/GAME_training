# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:13:51 2020

@author: ashkans
"""

#imports
from GAME.assignment import Assignment
from os.path import join
import os
import sys

#inputs
Question_DB = r"C:\Users\ashkans\Documents\git\GAME_database"
output_dir = r"C:\Users\ashkans\Documents\git\GAME_test_output"
sys.path.append(join(Question_DB))

# The number of assignment, to be shown in the pdfs
assignment_num = 1
# set the list of question from question database to be used
Qlist = ['A1Q1'] 
# name 
name = 'Week 1'

sid = '0000000'

A_dir = join(output_dir,'Assignment_%s' % assignment_num)
output_path = join(A_dir, 'A%d_%s' % (assignment_num, sid))
if not os.path.isdir(output_path):
    os.makedirs(output_path)

# initialize the assignment class
assignment1 = Assignment(Question_DB, Qlist,name=name ,assignment_num=assignment_num-1)
# generate the questions
assignment1.generate_question_list()
# save input files (is needed for marking)
assignment1.save_input_files(output_path)
# save save tex file
assignment1.make_pdf(join(output_path,'Assignment%d.tex'%assignment_num))
# save assignment
assignment1.save(join(output_path,'Assignment_class.yml'))
    
