import argparse
import sys

def cal(args)
    if --o=='add':
        return args.x+ args.y
    elif --o=='mul':
        return args.x* args.y
    elif --o=='sub':
        return args.x- args.y
    elif --o=='div':
        return args.x/ args.y
    else:
        return "Something wrong"

if __name__ == '__main__':
    parser= argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=2.0, help="Enter 1st No")
    parser.add_argument('--y', type=float, default=2.0, help="Enter 2nt No")
    parser.add_argument('--o', type=str, default="add", help="Operation")
    args=parser.parse_args()
sys.stdout.write(str(cal(args)))