import os

def organize():
    infile = open('Raw Data.txt', 'r')
    myData = infile.readlines()

    index = 0
    while index < len(myData):
        myData[index] = myData[index].rstrip('\n')
        index += 1
    #print(myData)
    studid = myData[0] ##Notice The student ID is the first object which we will use below

    del myData[0] #deleted from the original list

    responseList = [(myData[0])]
    #print(timeList)
    for i in range(len(myData)):
        if i % 2 == 0:
            responseList.append(myData[i])
    #print(responseList)
    del responseList[0]
    del responseList[0]

    save_path = 'C:/Users/emily/Desktop/PSYC15_Project_dynamic1//' + studid
    completeName = os.path.join(save_path, 'Response' + studid + '.txt')
    outfile = open(completeName, 'w')
    outfile.write("Responses:\n\n")
    count = 1
    for num in responseList:
        outfile.write(str(count) + ") " + str(num) + '\n')
        count += 1
    outfile.close()

if __name__ == "__main__":
    organize()
