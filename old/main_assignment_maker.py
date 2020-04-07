#imports

from GAME.assignment import Assignment
from os.path import join
import os
import sys





#inputs
Question_DB = r"C:\Users\ashkans\Documents\git\GAME_database"
output_dir = r"C:\Users\ashkans\Documents\git\GAME_test_output"


sys.path.append(join(Question_DB))

Qdict = {1:['A1Q1'],
         2:['A2Q1','A2Q2','A2Q3','A2Q4','A2Q5'],
         3:['A3Q1'],
         4:['A4Q1','A4Q2','A4Q3','A4Q4'],
         5:['A5Q1','A5Q2'],
         7:['A7Q1'],
         99:['A99Q1']}

name_dict = {1:'Week 1',
             2:'Week 2',
             3:'Week 3',
             4:'Week 4',
             5:'Week 5',
             7:'Week 7',
             99:'Week 99'}

SID = ['10','20','30']
assignment_num = 1



for assignment_num in Qdict:
    Qlist = Qdict[assignment_num]
    
    for sid in SID:
        A_dir = join(output_dir,'Assignment_%s' % assignment_num)
        output_path = join(A_dir, 'A%d_%s' % (assignment_num, sid))
        
        
        if not os.path.isdir(output_path):
            os.makedirs(output_path)

        # initialize the assignment class
        assignment1 = Assignment(Question_DB, Qlist,name=name_dict[assignment_num],assignment_num=assignment_num-1)
        # generate the questions
        assignment1.generate_question_list()
        # save input files (is needed for marking)
        assignment1.save_input_files(output_path)
        # save save tex file
        assignment1.make_pdf(join(output_path,'Assignment%d.tex'%assignment_num))
        # save assignment
        assignment1.save(join(output_path,'Assignment_class.yml'))
        
