# -*- coding: utf-8 -*-
# @Date     : 2017-05-09 13:06:56
# @Author   : Alan Lau (rlalan@outlook.com)
# @Language : Python3.5

from fwalker import fun
import random
from reader import writetxt, readtxt
import shutil
import os


def main():
    filepath = r'..\email'
    testpath = r'..\test'
    files = fun(filepath)
    random.shuffle(files)
    top10 = files[:10]
    for ech in top10:
        ech_name = testpath+'\\'+('_'.join(ech.split('\\')[-2:]))
        shutil.move(ech, testpath)
        os.rename(testpath+'\\'+ech.split('\\')[-1], ech_name)
        print('%s moved' % ech_name)


if __name__ == '__main__':
    main()
