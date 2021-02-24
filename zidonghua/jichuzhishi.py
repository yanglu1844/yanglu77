# print('hello word')
#
# # 变量和赋值：
# name='yanglu'  # name是变量名，yanglu是变量值
# name='123'
# print(name)
# name='1.3'
# print(type(name))
# name='yanglu111'
# print(name,type(name))
#
# # 增量赋值：
# name=1.5
# print(name)
# name=3*name    #等价于 name*=3
# print(name)
# name+=5         #等价于name=5+name
# print(name)


# # 认识数字：
# name=5  #int 转化为float
# print(name,type(name))
# name=float(name)
# print(name,type(name))
# name=float(name)
# print(name,int(name))
#
# name=5.99   #(转化为int，直接舍掉小数位)
# name=int(name)
# print(name,type(name))
#认识字符串:
# （字符串可以用单引号，双引号，三引号）
# name_1='yanglu1'
# name_2="yanglu2"
# name_3='''yanglu3'''
# print(name_3)
#
# #想展示双引号内容的话就在外面用单引号
# name_4='"yanglu4"'
# name_5='a b c "yanglu05" d e f'
# print(name_4,name_5)
#
# #换行符：\n  (如果想要打出\n则多打一个\,输入\\n)
# name_6='ab cd ef gh \nyanglu ij kl mn'
# name_7='we rt yy ui\\nyanglu opkj'
# print(name_6)
# print(name_7)
#
# #切片：
# # 从字符串里取一些想要的内容
# name_8='wertyyuinyangluopkj'
# print(name_8[0])  #取字符串的第1个元素
# print(name_8[1])  #取字符串的第2个元素
# print(name_8[-1])  #取字符串的第倒数第1个元素
# print(name_8[-2])  #取字符串的第倒数第2个元素
# print(name_8[0:3])  #取字符串的第1个d到第3个元素，左闭右开
# print(name_8[1:4])  #取字符串的第2个d到第4个元素，左闭右开
# print(name_8[1:-1])  #取字符串的第2个d到倒数第2个元素，左闭右开
# print(name_8[1:])  #取字符串的第2个d到最后一个元素
# print(name_8[:5])  #取字符串的第1个d到第5个元素，左闭右开
# print(name_8[:])  #取全部元素
#
# print(name_8[::-1]) # 将字符串反转
# print(name_8[::2])  #中间间隔1位
# print(name_8[::3])  #中间间隔2位
# print(name_8[::-2])  #反向-中间间隔1位
# print(name_8[::-3])  #反向-中间间隔2位
#
# # 字符串也可以用加法和乘法
# #加法
# name_9='yang'
# name_10='lu'
# print(name_9+name_10)
# print('yangyang'+'lulu')  #字符串加字符串是一个拼接的过程，无缝连接
# print('yangyang','dadada'+'lulu') #加逗号有空格
#
# #乘法
# print('yangyang'*2)
# print('fa'*10)
#
# #用内建函数len获取字符串长度
# print(len('yanglu'))
# print(len('yanglu'*10))
#
# #格式化
# name='yanglu'
# num=1
# print('欢迎您：%s,您是今天第%d个登录者'%(name,num))
# name='yuhaihua'
# num=2
# print('欢迎您：%s,您是今天第%d个登录者'%(name,num))


# 认识布尔类型（True和False)  True=1,False=0
# a=True
# b=False
# print(type(a),type(b))
# print(a*b)
# print(1*a)
# print(2*b)



# #输入和输出
# # input是请用户输入，input接收的是字符串
# name=input ("请输入您的名字:")    #提示用户输入
# num=int(input ("请输入您的数字:"))
# print(type(name))
# print('欢迎您：%s,您是今天第%d个登录者'%(name,num))

# print('123',end='\n')  #123后面默认有个end='\n'
# print('456')
#
# print('123',end='-')  #123输出完成之后加个横线，与下个输出一起输出
# print('456')
#
# print('789',end='。')  #123输出完成之后加个。
# print()   #(空，换下一行)
# print(333)



#整行注释：ctrl+/

#查看系统编码方式：
# import sys
# print(sys.getdefaultencoding())

#python2默认编码方式不是utf-8,python3的默认编码方式是utf-8
#如果要包含中文，默认不是utf-8的话，需要在代码文件最开头的地方注明： -*- coding: UTF-8-*-

#操作符
#+ - * / %（加 减 乘除 取余）
# print(3/2)  #3除2
# print(25%3)   #取余
# print(5//2)   #地板除，只保留整数位
# print(5//-


#**表示乘方运算
# print(3**2)  #3的平方
# print(3**4)  #3的四次方
#
# a=4
# b=3
# print(a**b)   #a的b次方

#比较运算符：<(小于）  > (大于)  <=(小于等于）   >= (大于等于）  == (等于）   != (不等于）  (是一个布尔值）
# print(2>4)
# print(3==4)
# print(3!=4)

#逻辑运算符：and  or  not
# print(2>4  and 2<4)
# print(2>4  or 2<4)
# print(not 2>4)

#字符串间也可以比较大小：数字<A<Z<a<z

#原始字符串：给字符串前面加r
# print(r'hello \n world')

#列表和元组
# a=[]
# b=()
# print(type(a),type(b))
#
# c=[1,3,444,'yang',34,'lu',(5,6,8,'ff')]   #列表里面可以套元组
# d=(1.22,4,77,[1.2,6,8,'ggg'])   #元组里面可以套列表
# print(c[2])
# print(d[3])
# print(d[-1])
# print(d[-1][1])

#排序： sort是升序
# # 数字类型的
# a=[2,8,4,6,9]
# print(sorted(a))   #a的本身没有发生变化
# print(sorted(a,reverse=True))   #a的本身没有发生变化,加个reversr=True是按照降序排列
# print(a)
# a.sort()       #a的本身发生了变化
# print(a)
# a.sort(reverse=True)       #a的本身发生了变化,加个reversr=True是按照降序排列
# print(a)
# #字符串类型的
# b=['d','qqq','rwv','ffa']
# print(sorted(b))
# print(sorted(b,key=len,reverse=True))  #加key=len按照长度送小到大排列，在加reverse=True按照降序排列


#列表和元组唯一的区别是：列表的元素可以修改，但是元组中的元素不能修改
# c=[1,3,444,'yang',34,'lu',(5,6,8,'ff')]
# c[0]=100
# print(c)   #列表的元素可以修改，按下标取值
# d=(1.22,4,77,[1.2,6,8,'ggg'])
# #d[0]=300
# #print(d)
# #元组的元素不能修改，会报错
# #如果元组中含有列表，则可以更改列表中的元素,不可以将列表赋值
# d[3][1]=10
# print(d)

#字典
#字典是键值对（key:value),列表不可以做key,元组和布尔值可以做key
#字典不按下标取值，按照key取值
# zidian1={'yang':1,'lu':2,'yu':3}
# print(zidian1['yang'])

# zidian2={(6.7,5,888):1,'lu':2,'yu':3}  #字典的key值可以用元组
# print(zidian2[(6.7,5,888)])

# zidian3={True:1,'lu':2,False:3}  #字典的key值可以用布尔值
# print(zidian3[True])

# zidian4={'yang':1,'lu':2,'yang':3}  #字典的key值如果相同，则取后面的key值，相当于去重的效果
# print(zidian4['yang'])

#zidian5={'lulu':{'age':18,'sex':'女','weight':90}}  #字典里可以嵌套字典
# print(zidian5)
# print(zidian5['lulu'])
# print(zidian5['lulu']['sex'])

# zidian5['yuyu']={'haha':{'age':18,'sex':'女','weight':90}}  #在原有的字典上新增元素，如果存在key值相同，则修改键值
# print(zidian5)

# del zidian5['yuyu']   #使用del删除某一个键值对，取key值删除
# print(zidian5)

# zidian5.clear()   #使用clear清空字典
# print(zidian5)

# zidian6={'lulu':{'age':18,'sex':'女','weight':90},'yang':'kkk'}
# zu=zidian6.pop('lulu')  #使用pop删除键值对，同时可以获取到值
# print(zu)
# print(zidian6)

# zidian7= {'lulu': {'age': 18, 'sex': '女', 'weight': 90}, 'yang': 'kkk'}
# print(zidian7.keys())  #返回一个列表，包含字典的所有key
# print(zidian7.values())  #返回一个列表，包含字典的所有values
# print(zidian7.items()) #返回一个列表，每一个元素都是一个元组，包含了key和value


#字符串的合并和拆分
# a='---'
# b=['tt','wwvgs','ywhxh','gwgb']
# print(a.join(b))   #把列表b按照a合并成一个字符串
#
# a=''
# b=['tt','wwvgs','ywhxh','gwgb']
# print(a.join(b))   #把列表b按照a合并成一个字符串，像糖葫芦一样串起来，没有规律
#
# c='tt---wwvgs---ywhxh---gwgb'
# print(c.split('---'))   #把字符串c按照---拆分成列表


# 字符串的常用函数
# 判定字符串开头结尾
# a='hello world my name is yanglu'
# print(a.startswith('hel'))
# print(a.endswith('hel'))
#
# #去除字符串开头结尾的空格
# a='     hello world my name is yanglu           '
# print(a,'bcbx')
# print(a.strip(),'bcbx')
#
# #查找字符串的子串
# a='hello world my name is yanglu'
# print(a.find('lo'))  #查找lo的下标,只取l的下标
# print(a.find('lo0'))  #查找的字符串中不包含lo0,则返回-1
#
# #统计字符串的里的字符出现的次数
# a='hello world my name is yanglu'
# print(a.count('l'))  #查找l出现了几次
#
# #把字符串替换成别的字符串
# a='hello world my name is yanglu'
# print(a.replace('lo','yanglu'))   #a不发生改变
# print(a)
#
# b=a.replace('lo','yanglu') #给a重新赋值
# print(b)
#

#判定字符串是字母/数字
#str.isalpha如果字符串至少有一个字符并且所有字符都是字母则返回True
#str.isdigit如果字符串只包含数字则返回True否则返回False
# a='hello world my name is yanglu'
# print(a.isalpha())
# b='1234'
# print(a.isdigit())

#
# #列表常用操作
# #append：追加元素
# a=[1,2,4,'ttt']
# a.append('yang')
# print(a)
#
# #删除指定下标元素
# b=[1,2.99,4,'tuutt']
# del b[0]
# print(b)
#
# #按值删除元素
# c=[1,2.99,4,'tuutt']
# c.remove(4)
# print(c)

#列表比较大小
# a=['abc',1234]
# b=['tesc',154]
# c=['abc',134]
# print(a>b)
# print(a>c)
# print(c>b)


#对象三要素：id type value  面向对象编程，万物皆是对象
#赋的值是对象，相同的对象三要素都一样
# a=100   #a引用了100
# print(id(a),type(a),a)
# b=100
# print(id(b),type(b),b)
# b=200
# print(id(b),type(b),b)
# b=True
# print(id(b),type(b),b)


#
# #if语句
# if 3>2:   #if语句可以独立运行，如果表达式的值非0或者为True,则执行if下面的内容
#     print('yanglu')
#
# #if语句也可以加else
# if []:  #如果if语句的值成立，则输出内容，不成立则输出else的内容，if和else一定会执行1个且只执行1个
#     print('yang')
# else:
#     print('lu')
#
# #if语句也可以加elif(否则如果）
# score=44  #score是变量值
# if score>=85:
#     print('你的成绩是优秀')
# elif score>=70:
#     print('你的成绩是良好')
# elif score >= 60:
#     print('你的成绩是良好')
# else:
#     print('你的成绩是不及格')


# #代码及缩进
# x,y=-3,-4
# # x,y=y,x  #两个变量互换值
# # print(x,y)
#
# if x<0:
#     if y>0:
#         print('yanglu')
#     else:
#         print('haihua')
# else:
#     print('zicheng')
#
# #最小值
# a,b=2,6
# if a<b:
#     smaller=a
# else:
#     smaller=b
# print(smaller)


#while循环：和if语句语法类似，只要表达式的值非0或者为True,就会循环执行
# n=1
# while True:
#     print(111,n)
#     n+=1     #每循环一次+1

# n=10
# while n<30:  #输出的值小于30时就不要循环了
#     print(111,n)
#     n+=1     #每循环一次+1

# n=1
# b=True
# while b:
#     if n>10:
#         b=False
#     print(111,n)
#     n+=1     #每循环一次+1


#for循环
# name='yanlu'
# for n in name:   #拆分字符串，循环了几次
#     print(n)
#
# list=[1,3,5,'ddd']   #按列表元素一个一个拆分
# for m in list:
#     print(m)
#
# yuanzu=(2,32,56,'yf')  #按元组里的元素一个一个拆分
# for m in yuanzu:
#     print(m)

# zidian={'y':123,'l':'fv','as':'sss'}  #拆分字典里的元素
# for k in zidian:
#     print(k)        #输出的是key,默认和下面的一样
# for k in zidian.keys():
#     print(k)
#
# for v in zidian.values():   #输出的是键值
#     print(v)
#
# for z in zidian.items():   #输出的是键值对
#     print(z)
#
# for w,y in zidian.items():   #w是key,y是value
#     print(w,y)

# #内建函数range
# print(list(range(1,7)))  #左闭右开
# for n in range(1,7):
#     print(n)
# for n in range(7):#取大于等于0小于7，给几就是循环几次
#     print(n)
# for n in range(2,71,3):  #取2到6，中间间隔2个
#     print(n)
# liebiao=[1,4,6,10,'yang','lu']
# for n in range(len(liebiao)):#输出的是liebiao的下标:range(4)
#     if liebiao[n]=='yang':
#         liebiao[n]='yu'
#     print(liebiao)

#常用内置函数：
# abs:求一个参数的绝对值
# a=-10
# print(abs(a))
# print(abs(-55))
# #divmod:返回一个元组，同时计算商和余数
# a,b=divmod(10,3)
# print(a,b)
# print(divmod(20,3))
# #round:对浮点数进行四舍五入，round有两个参数，第一个是进行运算的值，第二个是保留小数点后多少位
# print(round(5.2525475775,5))
# a=round(2.9793573956,3)
# print(a)

#查找[1，100)第一个3的倍数
#%3==0就是3的倍数
#从1开始
#找到1个符合的就停下来,使用break跳出当前循环
# for n in range(5,100):
#     #print(n)
#     if n%3==0:
#         print(n,'是3的第一个倍数')
#         break   #只要有一个满足，就停下来

#使用continue语句，回到循环顶端，判定循环条件
# for n in range(5,100):
#     #print(n)
#     if n%3!=0:
#         continue
#         print(n,'不是3的第一个倍数')
#     print(n)
#
# #pass语句，有时候需要用到空语句这样的概念，
# for n in range(5,100):
#     if n%3!=0:
#        pass
#     else:
#         print(n,'是3的第一个倍数')


#生成[0,4)的数字的平方列表
# a=[n**2 for n in range(4)]
# print(a)

#获取[0,8)区间中的所有奇数
# b=[x for x in range(8) if x%2==1]
# print(b)
# #等价于下面
# c=[]
# for x in range(8):
#     if x%2==1:
#         c.append(x)
# print(c)


#使用def来定义一个函数，使用ruturn来返回结果
# def jiafa(x,y):  # x,y是形参，
#     return x+y     #返回x+y的结果
# l=jiafa(3,5)       #3,5是实参
# print(l)
#
# def jiafa(x=4,y=8):  # x,y是形参，可以四默认值
#     return x+y     #返回x+y的结果
# l=jiafa()
# print(l)
#
#
# #综合运算
# def zonghe(x,y):
#     return x+y,x-y,x*y,x/y
# a,b,c,d=zonghe(5,2)
# print(c)
# _,_,d,_=zonghe(10,4)   #_是占位符
# print(d)
#
# #算税
# def shuihou(money):
#     if money>10000:
#         mymoney=money-money*0.1
#     elif money>5000:
#         mymoney = money - money * 0.03
#     else:
#         mymoney=money
#     return mymoney
# my_money=shuihou(18000)
# print(my_money)
# my_money=shuihou(8000)
# print(my_money)
# my_money=shuihou(4000)
# print(my_money)



#不定长函数
# def qiandao(persons):
#     print('参加我婚礼的朋友:',persons)
# qiandao('yanglu')

#如果是有多个人来参加婚礼，在persons前面加*
# def qiandao(*persons):
#     print('参加我婚礼的朋友:',persons)
# qiandao('yanglu','zicheng''haihua')
#
# def xinxi(name,**personsxinxi): #存储的是键值对形式
#     print(name,'的详细信息:',personsxinxi)
# xinxi('yanglu',a='我是大学同学',b='我随礼金3000')


#作用域
# def suibian(x):
#     y=2
#     print(x+4)
# suibian(10)    #如果输出print(y)会报错
# def suibian(x):
#     global y
#     y=4
#     print(x+4)
# suibian(10)    #如果输出print(y)会报错
# print(y)


#读文件:
#相对路径
# a=open('duwenjian','r',encoding='utf-8')  #相对路径，打开这个文件，以读的形式,a是变量
# for b in a:
#     print(b)    #直接print得出的是换了2行
#     print(b.strip())  #去掉换行符等价于下面的
#     print(b,end='')
#绝对路径
# a=open(r'C:\Users\yanglu\PycharmProjects\yanglu-test001\duwenjian','r',encoding='utf-8')  #绝对路径，打开这个文件，以读的形式,a是变量
# for b in a:
#     print(b)    #直接print得出的是换了2行

# a=open('duwenjian','r',encoding='utf-8')
# # print(a.read(4))   #从开始读指定长度为4的字符
# print(a.read(9))
# a.close()   #读完关闭文件
# a=open('duwenjian','r',encoding='utf-8')
# print(a.readline())  #读一行的内容，读过的不能在被读到
# #print(a.readlines())  #读所有行的内容，读过的不能在被读到

#写文件：a 追加写（不修改之前的内容，继续写）
# b=open(r'C:\Users\yanglu\PycharmProjects\yanglu-test001\files\xiewenjian','a')
# b.write('yanglu\n')
# #覆盖写(清空文件再写）
# b=open(r'C:\Users\yanglu\PycharmProjects\yanglu-test001\files\xiewenjian','w')
# b.write('zichdslbflsbvjshgsb\n')
# b.close()

#with open(会自动关闭文件）
# with open(r'C:\Users\yanglu\PycharmProjects\yanglu-test001\files\xiewenjian','w') as c:
#     c.write('fsfsdgsbfdbkdbf')


#处理异常（前面出错了，后面就不运行了）
# list=[1,4,6]
# try:
#     print(list[9])
#     a=open('files\dwenjian','r',encoding='utf-8')
# except:
#     print('错了')

class buy_house():
    def __int__(self,mianji):
        self.mj=mianji


    kaifashang='四季都会'
    def jiage(self):
        print('上海房子的最近价格为4万元每平')

yanglu=buy_house(100)
print(yanglu.mj)
print(yanglu.kaifashang)
yanglu.jiage()

zicheng=buy_house(200)
print(zicheng.mj)
print(zicheng.kaifashang)
zicheng.jiage()



























