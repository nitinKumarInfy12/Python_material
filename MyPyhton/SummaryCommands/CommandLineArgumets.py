# need to import argparse
# argparse helps in parsing teh parameters passed through the command line
# add the ArgumentParser() class from teh argparse module
# to parse the argumnets , need to use parse_args() method

import argparse

if __name__=='__main__':
   # initialize the parser
    parser = argparse.ArgumentParser(
        description= "my match script" # this description will be shown in help -h
    )

   # add the parameters positional/optional
    parser.add_argument('--num1',help ="number 1", type=float) # by default the arguments are positional. to make them optional make usse of "--" in front of te parameter name
    # short hand notation can also be added to the arguments as well as the '-" to make that optional
    parser.add_argument('-n1','--num1', help="number 1", type=float)

    parser.add_argument('-n2','--num2', help='number 2', type=float)

    parser.add_argument('-O','--operator', help='provide operator', default='+') # default type is string, default is teh keyword to provide default argument

   #parse the arguments
    args = parser.parse_args()
    print(args) # prints teh arguments passed by the command line

    Result = None
    if args.operator == '+':
        Result = args.num1 + args.num2
    if args.operator == '-':
        Result = args.num1 - args.num2
    if args.operator == '*':
        Result = args.num1 * args.num2
    if args.operator == '/':
        Result = args.num1 / args.num2

    print(Result)
#C:\Users\nkum17\PycharmProjects\MyProject\CommandLineArgumets.py

# command line
# when passed arguments through the command line: Make note of it.
# when argments ar epassed without the argument name then its positional argument
# 1. when used withoud short hand notation. then the argumants has to be passed with space if passed along with optional argument name
# ex: --num1 20 num2 40 --operator +
# 2. if short hand notation is used, then in place of space, = sign has to be used
# ex: -n1=20 -n2=30 -o=+