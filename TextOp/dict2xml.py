#!/usr/bin/env python
# coding=utf-8
from xml.etree.ElementTree import Element,SubElement,tostring
from xml.dom.minidom import parseString
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

books=Element('books')
for isbn,info in BOOKS.iteritems():
    book=SubElement(books,'book')
    info.setdefault('author','Wesley Chun')
    info.setdefault('edition',1)
    for key,val in info.iteritems():
        SubElement(book,key).text=','.join(str(val).split(':'))

xml=tostring(books)
print '***PERTTY-PRINTED XML'
print xml

print '\n*** FLAT STRUCTURE***'
for elem in books.getiterator():
    print elem.tag,'-',elem.text

print '\n ***TITLE ONLY***'
for books in books.findall('.//titile'):
    print book.text
