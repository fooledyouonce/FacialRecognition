import os
from openpyxl import *

def calcData():
    infile = open('Raw Data.txt', 'r')
    myData = infile.readlines()

    index = 0
    while index < len(myData):
        myData[index] = myData[index].rstrip('\n')
        index += 1
    #print(myData)
    studid = myData[0] #Notice The student ID is the first object which we will use below

    del myData[0] #<-- i then delete it from the original list
    #print(myData)
    
    timeList = [float(myData[0])]
    for i in range(len(myData)):
        if i % 2 != 0:
            timeList.append(float(myData[i]))
    #print(timeList)

    elapList = []
    index1 = 0
    while index1 < len(timeList)-1:
        elapList.append(timeList[index1 + 1] - timeList[index1] - 5.5)
        index1 += 1
    #print(elapList)

    save_path = 'C:/Users/emily/Desktop/PSYC15_Project_dynamic1//' + studid
    completeName = os.path.join(save_path, 'Time' + studid + '.txt')
    outfile = open(completeName, 'w')
    outfile.write("Elapsed time in seconds\n\n")
    count = 1
    for time in elapList:
        outfile.write(str(count) + ")   " + str(time) + '\n')
        count += 1
    outfile.close()

    #Writing the time data into the user excel file, inside the user folder
    excel = load_workbook('C:/Users/emily/Desktop/em_recog_dynamic.xlsx')
    data_sheet = excel[studid]
    
    count = 0
    time_row = 2
    for i in elapList:
        data_sheet.cell(row = time_row, column = 2).value = round(i,3)
        count += 1
        time_row += 1

    excel.save( 'C:/Users/emily/Desktop/em_recog_dynamic.xlsx' )

if __name__ == "__main__":
    calcData()
