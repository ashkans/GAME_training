# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:07:51 2020

@author: ashkans
"""

#import assignment_maker

from GAME.assignment import  load_assignment
from os.path import join


#inputs
Question_DB = "QuestionDB"
output_dir = "..\\..\\test_output"

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

SID = ['10']

for assignment_num in Qdict:
    Qlist = Qdict[assignment_num]
    for sid in SID:
        A_dir = join(output_dir,'Assignment_%s' % assignment_num)
        output_path = join(A_dir, 'A%d_%s' % (assignment_num, sid))
        assignment = load_assignment(join(output_path, 'Assignment_class.yml'))
        resutls_path = []
        for q in assignment.questions:
            q.text.inputs = q.marking.input_loader(join(output_path,'%s_input.csv' % q.qid))
            if assignment_num != 2:
                x = q.qid
            else:
                x = 'A2Q1'
            resutls_path.append(join(output_path,'%s_answer.xlsx' % x))
        assignment.mark_and_get_feedbacks(resutls_path)
        assignment.write_feedback_file(join(output_path,'feedback.tex'), name=name_dict[assignment_num],assignment_num=assignment_num-1)