import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=1.0,
                        help="What is your first number ?")
    parser.add_argument("--y", type=float, default=1.0,
                        help="What is your second number ?")
    parser.add_argument("--operation", type=str, default="add",
                        help="What Opreation ? Choose from add, sub, mul, or div")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    operation = args.operation
    x, y = args.x, args.y
    
    if operation == "add":
        return x + y
    elif operation == "sub":
        return x - y
    elif operation == "mul":
        return x * y
    elif operation == "div":
        return x / y
        
if __name__ == "__main__":
    main()
    


# Now, via the command line, we can do something like:

# python file_name.py --x=5 --y=3 --operation=mul
# You should get 15.0 returned via the command line in this case. Another thing we can do is:

# python file_name.py -h

# Output:

# usage: argparse_example.py [-h] [--x X] [--y Y] [--operation OPERATION]

# optional arguments:
#   -h, --help            show this help message and exit
#   --x X                 What is the first number?
#   --y Y                 What is the second number?
#   --operation OPERATION
#                         What operation? Can choose add, sub, mul, or div