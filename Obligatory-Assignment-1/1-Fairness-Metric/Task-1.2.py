import argparse
from decimal import Decimal, getcontext
getcontext().prec = 50

#Checking what type of unit and returning the answer
def checkType(val):
    kilo='Kbps'
    mega='Mbps'
    giga='Gbps'

    if kilo in val:
        return kilo
    elif mega in val:
        return mega
    elif giga in val:
        return giga

#Converting the num based on the type
#Converting all of them to bps to compare later
def convert(num, type):
    numDec=Decimal(num)

    if type == 'Kbps':
        numDec=numDec*Decimal(1000)
        return numDec
    elif type == 'Mbps':
        numDec=numDec*Decimal(1000000)
        return numDec
    elif type == 'Gbps':
        numDec=numDec*Decimal(1000000000)
        return numDec

def jfi(list):
    sumList=sum(list) #Sums the values in list
    listLength=len(list) #Finds the length of the list
    jfiFormula=(sumList ** 2)/(listLength * sum(i ** 2 for i in list))
    return jfiFormula

def main():
    parser=argparse.ArgumentParser(description='Finds the JFI of accepted throughout-list')

    #Using nargs so the argument expects more than one input value
    parser.add_argument('throughput_file', help='File of throughputs')

    args=parser.parse_args()

    throughputList=open(args.throughput_file, 'r')

    convertedList=[] #List that will hold on the converted values
    list=[]
    num='' #Variable that will hold on the put-together-num from the given file
    type='' #Saving the type of unit so we can use it for right conversion

    for i in throughputList: 
        list.append(i)
        type=checkType(i) #Saving the unit type for later use
        for j in i:
            if j.isdigit(): #Checking if the chars in i contains integers
                num=num+str(j) #If so we'll put together the integers as string
            elif j == 's': #When we come to the end of unit for instant Kbp[s], Mbp[s], Gbp[s]
                converted=convert(num,type)
                convertedList.append(float(converted)) #Adding the converted values to the list
                num='' #Emtying the variable num

    throughputList.close() #Closing the opened file  
    result=jfi(convertedList)
    print(f"Jains Fairness index is:  {result}")

main()