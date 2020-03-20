#while 循环
# condition=1
# while condition<10:
#     print(condition)
#     condition=condition+1


#for 循环
# example_list=[1,2,3,4,5,6,7,8,92,3,4,56]
# for i in example_list:
#     print(i)
#     print('inner of for')
#
# print(example_list)

# for i in range(0,10,5):
#     print(i)

#if 语句
# x=2
# y=2
# z=3
#
# #<= >= == != > <
# if x==y:
#     print('x is equal to y')

# # if else 语句
# x=4
# y=2
# z=3
# if x>y:
#     print('x is greater than y')
# else:
#     print('x is less or equal to y')

# # if elif else语句
# x=-2
# y=2
# z=3
# if x>1:
#     print('x>1')
# elif x<1:
#     print('x<1')
# elif x<-1:
#     print('x<-1')
# else:
#     print('x=1')
# print('finish running')

# #def 函数
# def function(a,b):
#     c=a+b
#     print(c)
#
# def func():
#     print('this is a function')
#     a=1+2
#     print(a)
#
# func()
# function(2,3)

# #def 函数参数
# def fun(a,b):
#     c=a*b
#     print('the c is ',c)
# fun(3,4)

# #def 默认参数
# def sale_car(price,brand,colour='red',is_second_hand=True):
#     print('price:',price,
#           'colour:',colour,
#           'brand',brand,
#           'is_second_hand',is_second_hand)
#
# sale_car(13100,'BMW','yellow')


# #全局  局部变量
# APPLE=100
# a=None
# def fun():
#     global a #全局变量
#     a=20
#     return a+100
#
#
# print(APPLE)
# print('a past=',a)
# print(fun())
# print('a now=',a)


# append_text='\n This is appended file'
#
# my_file=open('my file.txt','a')
# my_file.write(append_text)
# my_file.close()

#
# file=open('my file.txt','r')
# # content=file.readline()
# # second_read_time=file.readline()
# # #print(content,second_read_time)
# contents=file.readlines()
# print(contents)
# file.close()

#类  class
# class Calculator:
#     name='Good calculator'
#     price=18
#     def add(self,x,y):
#         print(self.name)
#         result=x+y
#         print(result)
#     def minus(self,x,y):
#         result=x-y
#         print(result)
#     def times(self,x,y):
#         result=x*y
#         print(result)
#     def divide(self,x,y):
#         print(x/y)
#
# calculate=Calculator()
# print(calculate.price)
# calculate.add(10,11)
# calculate.minus(10,11)
# calculate.divide(13,2)

# class Calculator:
#     name='Good calculator'
#     price=18
#     def __init__(self,name,price,hight,width,weight):
#         self.name=name
#         self.price=price
#         self.hight=hight
#         self.width=width
#         self.weight=weight
#     def add(self,x,y):
#         print(self.name)
#         result=x+y
#         print(result)
#     def minus(self,x,y):
#         result=x-y
#         print(result)
#     def times(self,x,y):
#         result=x*y
#         print(result)
#     def divide(self,x,y):
#         print(x/y)
#
# calculate=Calculator('Price',12,30,15,19)
# print(calculate.name)
# print(calculate.weight)

# a_input=int(input('Please give a number:'))
# if a_input==1:
#     print('This is a good one')
# elif a_input==2:
#     print('See you next time')
# else:
#     print('Good luck')
# print('This input number is:',a_input)

# #tuple list
# a_tuple=(1,2,3,5,23,45)
# another_tuple=1,2,3,5,23,45
#
#
# a_list=[1,2,3,5,23,45]
#
# # for content in a_list:
# #     print(content)
#
# # for index in range(len(a_list)):
# #     print('index=',index,'number in list=',a_list[index])
#
# for index in range(len(a_tuple)):
#     print('index=',index,'number in tuple=',a_tuple[index])

# a=[1,2,3,4,5,6,7,0,9,8,1]
# a.append(12)
# print(a)

# a.insert(1,0)
# print(a)

# a.remove(1)
# print(a)

# #打印最后一位数字
# print(a[-1])
#
# #打印前几位
# print(a[0:3])
# print(a[:3])
#
# print(a[1:3])
# print(a[3:])
#
# print(a[-3:])
#
# print(a.index(1))
#
# print(a.count(-1))
#
# a.sort()
# print(a)
#
# a.sort(reverse=True)
# print(a)

# #多维的列表
# #numpy pandas
# a=[1,2,3,4,5]
# multi_dim_a=[[1,2,3],
#              [2,3,4],
#              [3,4,5]]
# print(a[1])
# print(multi_dim_a[0])

# #字典
# a_list=[1,3,5,3,4,5,6]
# d={'apple':1,'pear':2,'orange':3}
# d2={1:'a',2:'b'}
# print(d['apple'])
# del d['orange']
# print(d)
# d['cola']=20
# print(d)
#
# directory={'apple':[1,2,3],'pera':{1:3,3:'a'},'orange':2}
# print(directory['pera'][1])

# #import 模块
# from time import *
#
# print(localtime())
# print(time())
#
#
# import Func1
#
# Func1.printdata('Hello Python')
#
# # while True:
# a=True
# while a:
#     b=input('type something')
#     if b=='1':
#         a=False
#     else:
#         pass  #什么都不做
# print('finish run')

#
# while True:
#     b=input('type something')
#     if b=='1':
#         continue
#     else:
#         pass
#     print('still in while')
#
# print('finish')


# #错误处理
# try:
#     file=open('eeee','r+')
# except Exception as e:
#     print('there is no file named as eeee')
#     response=input('do you want to create a new file')
#     if response=='y':
#         file=open('eeee','w')
#     else:
#         pass
# else:
#     file.write('ssss')
#     file.close()
#
# a=[1,2,3]
# b=[4,5,6]
# zip(a,b)
# list(zip(a,b))
# print(list(zip(a,b)))
# for i,j in zip(a,b):
#     print(i,j)
#
# print(list(zip(a,a,b)))
#
# fun2=lambda x,y:x+y
# print(fun2(2,3))
#
# map(fun2,[1],[2])
# print(list(map(fun2,[1,3],[2,5])))

# #拷贝
# import copy
#
# a=[1,2,3]
# b=a
# print(id(a))
# print(id(b))
# b[0]=11
# print(a)
# print(b)
#
# c=copy.copy(a)
# print(id(a)==id(c))
#
# a=[1,2,[3,4]]
# d=copy.copy(a)
# e=copy.deepcopy(a)
#
# import pickle
#
# a_dict={'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}
# # file=open('pickle_example.pickle','wb')
# # pickle.dump(a_dict,file)
# # file.close()
#
# with open('pickle_example.pickle','rb')as file:
#     a_dict1=pickle.load(file)
# print(a_dict1)


# #set 不同
# char_list=['a','b','c','c','d','d','d']
#
# print(type(set(char_list)))


import multiprocessing as mp


def job(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)


if __name__=='main':

    q=mp.Queue()
    p1=mp.Process(target=job,args=(q,))
    p2=mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1=q.get()
    res2=q.get()
    print(res1+res2)



















