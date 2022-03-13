# coding: utf-8
from subprocess import run


def main():
    cmd_str = 'python setup.py clean --all'
    res = run(cmd_str.split())
    # print(res.stdout)


if __name__ == '__main__':
    main()
