#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup,Extension
#大部分编译工作由setup()函数完成，在该函数之前的代码都只是预备步骤。为了构建扩展模块，需要为每个扩展创建一个Extension实例。因为这里这有一个实例，所以只需要一个Extension实例
#Extension('Extest',sources=['Extest2.c'])
#第一个参数是扩展的完整名称，以及该扩展中用于的高阶包，该名称应该使用完整额点分割表示方式。由于这里是一个独立的保，因此名称为Extest.source参数是所有源文件的列表
MOD='Extest'
setup(name=MOD,ext_modules=[Extension(MOD,sources=['Extest2.c'])])
