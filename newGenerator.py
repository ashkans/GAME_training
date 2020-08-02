import pandas as pd
import sys
from helper import (folderNameGenerator, setSeed, makeMasterFolder,
                    makeSubsetDir, initialize)

settingsFile = sys.argv[1]
#settingsFile = r'settings/Assign1.yaml'

studentIdListPath, dbPath, masterPath, settings = initialize(settingsFile)

asd = settings['assginmentSubsetDirectory']

# load student list
df = pd.read_csv(studentIdListPath)
       
# loop over the lines of df
for index, student in df.T.items():
    sid = student['ID number']
    studentFolderName = folderNameGenerator(student)
    setSeed(sid)
    
    #make path for the student in the master folder.
    makeMasterFolder(masterPath, studentFolderName, settings, dbPath, sid)
    makeSubsetDir(masterPath, studentFolderName, asd, settings['basePath'])    
    