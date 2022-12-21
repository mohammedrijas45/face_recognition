from datetime import datetime  # import date and time handling library

def markatt(name):
    with open ('attend.csv','r+') as f: # Import attend.csv file
        myDataList = f.readlines()      # Read every single lines
        # print(myDataList)
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')    # Write a Name date time to atend.csv file