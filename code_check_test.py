#!/usr/bin/env python3
import sys
from DM.src.play.code_check import CodeCheck
def main():
    code_checker = CodeCheck("GomokuG1.py", 15)
    if not code_checker.check_code():
        print(code_checker.errormsg)
    else:
        print('pass')

if __name__ == '__main__':
    main()


