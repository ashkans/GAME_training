#!/usr/bin/env python
# coding: utf-8

# In[21]:


# import modules
from GAME.assignment import Assignment
from os.path import join
import os
import sys
import time


# In[22]:


# setting the path of question data base

Question_DB = join(os.path.dirname(os.getcwd()), "GAME_database")

# seetin the path for the outputs (question pdf)
output_dir = "C:\\Users\\ashkans\\Documents\\git\\GAME_test_output"

# the questions are using some helper functions which are located in the path of Question_DB, so they should be accessible:
sys.path.append(join(Question_DB))


# In[36]:


# the assignment number, to be shown in the pdfs
assignment_num = 9

for sid in range(10):
    t = time.time()
    A_dir = join(output_dir,'Assignment_%s' % assignment_num)
    output_path = join(A_dir, 'A%d_%s' % (assignment_num, sid))
    if not os.path.isdir(output_path):
        pass
        #os.makedirs(output_path)

    assignment1 = Assignment(Question_DB, assignmentName="Colin")
    assignment1.compilers = ['pdflatex', 'pythontex' , 'pdflatex']
    assignment1.make_assignment_pdf_from_tex_file(join(output_path,'Assignment%d.pdf'%assignment_num))
        
    print("assignment is generated in %2.0f seconds" % (time.time() - t))
    