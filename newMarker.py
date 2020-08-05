import pandas as pd
from helper import (folderNameGenerator, setSeed, makeMasterFolder,
                    makeSubsetDir, initialize, findStudentFolder, dirCheck, pathModifier)
from os.path import join
from GAME.assignment import  load_assignment
from GAME.fileNameManager import FileNameManager
import sys

settingsFile = sys.argv[1]
#settingsFile = r'settings/Assign1.yaml'

studentIdListPath, dbPath, masterPath, settings = initialize(settingsFile)


resPath = pathModifier(settings['basePath'], settings['resultDirectory']) 
assignmentNum = settings['assignmentNum']
title = settings['assignmnetTitle']

fsd = settings['feedbackSubsetDirectory']

# load student list
df = pd.read_csv(studentIdListPath)
markList = pd.DataFrame(columns=['mark', 'letter mark', 'full name'])
       
# loop over the lines of df
for index, student in df.T.items():
    sid = student['ID number']
    studentMasterFolderName = folderNameGenerator(student)
    studentResultFolderName = findStudentFolder(student, resPath)
    
    if studentResultFolderName is not None:
        studentMasterPath = join(masterPath, studentMasterFolderName)
        studentResultPath = join(resPath, studentResultFolderName)
        
    
        assignment = load_assignment(join(studentMasterPath, 'Assignment_class.yml'))
 
    
        # results path
        resutls_path = []
    
        # load the inputs
        for q in assignment.questions:
            fnm = FileNameManager(sid, assignmentNum, q.qid)
            studentInputFilePath = join(studentMasterPath,fnm.getInputFileName())
            q.text.inputs = q.marking.input_loader(studentInputFilePath)
            
            studentResultFilePath = join(studentResultPath,fnm.getAnswerFileName())
            resutls_path.append(studentResultFilePath)
    
        # get feedback and mark
        assignment.mark_and_get_feedbacks(resutls_path)
    
        # write the feedback file
        feedbackPath = studentResultPath
        
        dirCheck(feedbackPath)
        studentFeedbackFileName = join(feedbackPath,fnm.feedbackFileName())
        assignment.make_feedback_pdf(studentFeedbackFileName, 
                                     name=title,
                                     assignment_num=assignmentNum)
        
        markList.loc[sid, 'full name'] = student['Full name']
        markList.loc[sid, 'mark'] = assignment.mark
        markList.loc[sid, 'letter mark'] = assignment.letterMark


        
        makeSubsetDir(resPath, studentResultFolderName, fsd, settings['basePath']) 
        
if 'marksOutputPath' in settings.keys():
    path_to_save = pathModifier(settings['basePath'], settings['marksOutputPath']) 
    markList.to_csv(path_to_save)
else:
    markList.to_csv('marks.csv')

print(markList)    