#!/usr/bin/env python
# coding=utf-8
from distutils.log import warn as printf
from json import dumps
from pprint import pprint

BOOKS={
    '0132269937':
    {
    'titile':'Core Python Programing',
    'edition':2,
    'year':2007
    },
    '0132356139':
    {
        'titile':'Python Web Development with Djano',
        'author':['Jeff Forcier','Paul Bissex',
                 'Wesley Chun']
    },
    '01371419':
    {
        'titile':'Python Fundamentals',
        'year':2009
    },
}

printf('*** Raw Dict')
print(BOOKS)

printf('***\n PERTTY_pERINTED DICT ***')
print(dumps(BOOKS,indent=4))

