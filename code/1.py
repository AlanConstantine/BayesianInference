# -*- coding: utf-8 -*-
# @Date     : 2017-05-08 22:32:48
# @Author   : Alan Lau (rlalan@outlook.com)
# @Language : Python3.5


def function():
    pass


def main():
    a = 0.001*(0.99/(0.99*0.001+0.01*(1-0.001)))
    print(a)


if __name__ == '__main__':
    main()
