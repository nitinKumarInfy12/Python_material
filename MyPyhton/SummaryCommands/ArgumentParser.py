import argparse

if __name__ == '__main__':

    # initialize the parser
    parser = argparse.ArgumentParser(
        description = "my test script"
    )

    # add the parameters positional / optional
    # positional arguments
    parser.add_argument('num1', help="Number 1", type=float)
    parser.add_argument('num2', help="Number 2", type=float)
    parser.add_argument('Operation', help="Provide operator")

    # parse the arguments
    args = parser.parse_args()
    print(args)
    # in the command line following command gives provides teh help
    # python file.py -h

    result = None
    if args.Operation == '+':
        result = args.num1 + args.num2
    if args.Operation == 'pow':
        result = pow(args.num1, args.num2)

    print(result)

# in the command line: pyhton filename.py 10 20 +   : will print 30


# optional aguments , denote it by adding -- in front of teh argument name

    parser.add_argument('--num1', help="Number 1", type=float)
    parser.add_argument('--num2', help="Number 2", type=float)
    parser.add_argument('--Operation', help="Provide operator", default='+')

# command line now : python filename.py --num1 10 --num2 20 --operation +
# or since default is also declared, we may not pass the operation
# command line now : python filename.py --num1 10 --num2 20


# short notations can also be provided with optional arguments
    parser.add_argument('-n','--num1', help="Number 1", type=float)
    parser.add_argument('-i','--num2', help="Number 2", type=float)
    parser.add_argument('-o','--Operation', help="Provide operator", default='+')
# command line now : python filename.py -n=10 -i=20 -o=+