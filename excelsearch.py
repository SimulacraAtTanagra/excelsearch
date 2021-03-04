import pandas as pd 
import os


def filesearch(workbookName,particularString):
    dfwork = pd.read_excel(workbookName)
    if particularString in dfwork.values:
        print(workbookName)
        
def main(directory_in_str,term):
    directory = os.fsencode(directory_in_str)           #defines directory as indicated string
    os.chdir(directory)                                 #navigate to directory specified
    for file in os.listdir(directory):                  #iterates over all the files here
        filename = os.fsdecode(file)                    #specifies filename from file
        if filename[:-4] in ['xlsx','.xls']:
            fullpath =os.path.join(directory_in_str,filename)
            try:
                filesearch(fullpath,term)
            except:
                print(f'Search failed for {filename}')
                continue
    
