/*************************************************************************
	> File Name: Extest2.c
	> Author: 
	> Mail: 
	> Created Time: Thu 15 Nov 2018 07:01:17 PM CST
 ************************************************************************/

#include<stdio.h>
#include"Python.h"

int fac(int n){
    if(n<2 ) return 1;
    return n*fac(n-1);
}
/*
static PyObject* Extest_fac(PyObject *self,PyObject* args)
{
    int res;
    int num;
    PyObject *retval;

    res=PyArg_ParseTuple(args,"i",&num);
    if(!res)
    {
        return NULL;
    }
    res=fac(num);
    retval=(PyObject*)Py_BuildValue("i",res);
    return retval;
}
*/
static PyObject* Extest_fac(PyObject* self,PyObject* args)
{
    int num;
    if(!PyArg_ParseTuple(args,"i",&num))
    {
        return NULL;
    }

    return (PyObject*)Py_BuildValue("i",fac(num));
}
//这段代码会发生内存泄露：当Py_BuildValue将值组合到一个Python对象并返回时，它会创建传入数据的副本，在此处，创建了一对字符串，问题在于第二个字符串的创建，但在结束后没有释放这段内存，导致内存泄露
/*
static PyObject* Extest_doppel(PyObject* self,PyObject* *args)
{
    char *orig_str;
    if(!Py_ParseTuple(args,"s",&orig_str)) return NULL;
    return (Py_Object*)Py_BuildValue("ss",orig_str,reverse(strdup(orig_str)));
}
*/
char *reverse(char *s)
{
    register char t,*p=s,*q=(s+(strlen(s)-1));
    while(p<q)
    {
        t=*p;
        *p=*q;
        *q--=t;
    }
    return s;
}

static PyObject* Extest_doppel(PyObject* self,PyObject* args)
{
    char * orig_str;
    char *dupe_str;

    PyObject* retval;

    if(!PyArg_ParseTuple(args,"s",&orig_str))
    {
        return NULL;
    }
    retval=(PyObject*)Py_BuildValue("ss",orig_str,dupe_str=reverse(strdup(orig_str)));
    return retval;
}


int test(void )
{
    char s[BUFSIZ];
    printf("4!==%d\n",fac(4));
    printf("8!==%d\n",fac(8));
    printf("12!==%d\n",fac(12));

    strcpy(s,"madam");
    printf("reversing madam,we  get %s",reverse(s));
    return 0;
}


static PyObject* Extest_test(PyObject* self,PyObject* args)
{
    test();
    return (PyObject*)Py_BuildValue("");
}
//2.编写PyMethodDef MoudleMethods[]
static PyMethodDef
ExtestMethods[]={
    {"fac",Extest_fac,METH_VARARGS},
    {"doppel",Extest_doppel,METH_VARARGS},
    {"test",Extest_test,METH_VARARGS},
    {NULL,NULL}
};
//3添加模块初始化函数 void initModule(void)
void initExtest(void)
{
    Py_InitModule("Extest",ExtestMethods);
}

