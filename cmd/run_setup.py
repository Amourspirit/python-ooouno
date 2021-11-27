# coding: utf-8
from subprocess import run


def main():
    cmd_str = 'python setup.py sdist bdist_wheel'
    res = run(cmd_str.split(' '))
    # print(res.stdout)
    cmd_str = 'twine check dist/*'
    res = run(cmd_str.split(' '))
    # print(res.stdout)


if __name__ == '__main__':
    main()
