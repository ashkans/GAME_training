{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import modules\n",
    "from GAME.assignment import Assignment\n",
    "from os.path import join\n",
    "import os\n",
    "import sys\n",
    "import time\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "# setting the path of question data base\n",
    "\n",
    "Question_DB = join(os.path.dirname(os.getcwd()), \"GAME_database\")\n",
    "\n",
    "# seetin the path for the outputs (question pdf)\n",
    "output_dir = \"C:\\\\Users\\\\ashkans\\\\Documents\\\\git\\\\GAME_test_output\"\n",
    "\n",
    "# the questions are using some helper functions which are located in the path of Question_DB, so they should be accessible:\n",
    "sys.path.append(join(Question_DB))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "# student id, this could be loaded from a file\n",
    "sid = '00000'\n",
    "\n",
    "# the assignment number, to be shown in the pdfs\n",
    "assignment_num = 2\n",
    "\n",
    "# set the list of question from question database to be used\n",
    "Qlist = ['A1Q1'] \n",
    "\n",
    "# name \n",
    "title = 'Week 1'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\ashkans\\\\Documents\\\\git\\\\GAME_training'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\ashkans\\\\Documents\\\\git\\\\GAME_database'"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Question_DB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tex file is generated!\n"
     ]
    }
   ],
   "source": [
    "# maek sure that the output_dir exists and make the output file name\n",
    "A_dir = join(output_dir,'Assignment_%s' % assignment_num)\n",
    "output_path = join(A_dir, 'A%d_%s' % (assignment_num, sid))\n",
    "if not os.path.isdir(output_path):\n",
    "    os.makedirs(output_path)\n",
    "\n",
    "    \n",
    "# initialize the assignment class\n",
    "assignment1 = Assignment(Question_DB, Qlist,name=title ,assignment_num=assignment_num-1)\n",
    "\n",
    "# generate the questions\n",
    "assignment1.generate_question_list()\n",
    "\n",
    "# save input files (is needed for marking)\n",
    "assignment1.save_input_files(output_path)\n",
    "\n",
    "# save save tex file1\n",
    "assignment1.make_assignment_pdf(join(output_path,'Assignment%d.pdf'%assignment_num))\n",
    "\n",
    "# save assignment\n",
    "assignment1.save(join(output_path,'Assignment_class.yml'))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}