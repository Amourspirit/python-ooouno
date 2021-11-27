# coding: utf-8
from subprocess import run
TEST_MODULES = ['ooo_uno']
# kwhelp.method


def get_modules():
    global TEST_MODULES
    result = ''
    if len(TEST_MODULES) > 0:
        result = ' --cov=' + ' --cov='.join(TEST_MODULES)
    return result


def main():
    cov_mod = get_modules()
    # see: https://stackoverflow.com/questions/41748464/pytest-cannot-import-module-while-python-can
    cmd_str = f"python -m pytest{cov_mod} --cov-report=html"
    res = run(cmd_str.split(' '))
    if res.stdout:
        print(res.stdout)
    if res.stderr:
        print(res.stderr)
    print(cmd_str)


if __name__ == '__main__':
    main()
