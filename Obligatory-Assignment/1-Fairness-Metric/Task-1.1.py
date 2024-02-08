import argparse;

def jfi(list):
    sumList=sum(list) #Sums the values in list
    listLength=len(list) #Finds the length of the list
    jfiFormula=(sumList ** 2)/(listLength * sum(i ** 2 for i in list))
    return jfiFormula

def main():
    parser=argparse.ArgumentParser(description='Finds the JFI of accepted throughout-list')

    #Using nargs so the argument expects more than one input value
    parser.add_argument('throughput_list', nargs='+', type=int, help='List of throughputs')

    args=parser.parse_args()

    result=jfi(args.throughput_list)
    print(f"Jains Fairness index is:  {result}")

main()