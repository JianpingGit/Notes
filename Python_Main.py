* ##### 一些注意事项
```python
import sys; sys.version # 查看版本号
# python代码文件名，不要跟已安装模块重名
# python 大小写敏感
# python代码文件名，不要跟已安装模块重名
# 参数True必须写全，不能全部大写
# 字符串：单引号、双引号都可以
# \t : Tab
# \n : Enter
# 2**3 : 2的3次方
# 2进制是以0b开头的: 例如: 0b11 则表示十进制的3
# 8进制是以0o开头的: 例如: 0o11则表示十进制的9 
# 16进制是以0x开头的: 例如: 0x11则表示十进制的17
# _xxx 不能用’from module import *’导入
# __xxx__ 系统定义名字
# __xxx 类中的私有变量名
```
在函数内n+=1错误  
在函数内部对变量赋值进行修改后，该变量就会被Python解释器认为是局部变量而非全局变量，当程序执行到n+=1的时候，
因为这条语句是给n赋值，所以n成为了局部变量，那么在执行print n的时候，因为n这个局部变量还没有定义，自然就会抛出这样的错误。
那么，我们怎样才能达到在函数内部先打印，再赋值的操作呢？结论就是使用global关键字。

* ##### 包相关操作
```python
python setup.py install
pip install <package>  
# 直接删除Lip下的文件就可以删除包
```
---

* ##### 画图
```python
import matplotlib.pyplot as plt
 
```

* ##### os模块和sys模块的区别
os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口;  
sys模块负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境



* ##### ==python一些简化语句==
```python
a[::-1] #列表倒序排列
# if语句
name = 'wupeiqi' if 1 == 1 else 'alex'  
# 快速建list
ct = [random.randint(256) for x in range(3)] 
# lambda
# def func(arg):
#     return arg + 1 
my_lambda = lambda arg : arg + 1
result = my_lambda(123)
```
* ##### 颜色
RGB = (256,256,256)
十六进制表示 '#ffffff'
RGB转换为灰度=R*0.299+G*0.587+B*0.114


* ##### 格式符 百分号形式
格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:  
==%[(name)][flags][width].[precision]typecode==
```python
# (name)为命名
# flags可以有+,-,''或0。+表示右对齐正号，-表示左对齐，空格表示右对齐填充空格，0表示使用0填充。  
# width表示显示宽度
#precision表示小数点后精度
%s 字符串 (采用str()的显示)   
%d 十进制整数  
%o 八进制整数 
%x 十六进制整数 
%e 指数 (基底写为e) 
%E 指数 (基底写为E)  
%f 浮点数
%c Unicode单字符 
%% 字符"%"
"this is a test %010.3d" %(100)
"this is a test %(n)+10.3f" %{'n':100}
```

* ##### 格式符 format形式  
==[[fill]align][sign][#][0][width][,][.precision][type]==
```python
print('{0} is {0:>10.2f}'.format(1.123)) # 取2位小数，右对齐，取10位  
print('this is {} and {}'.format(1.123,10))  
print('{sb} is {nb}'.format(sb=1.123,nb=10))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# ^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。

# + 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格

# b、d、o、x 分别是二进制、十进制、八进制、十六进制。

# 此外我们可以使用大括号 {} 来转义大括号

```

* ##### 文件相关操作
```python
import os # 查看当前工作目录
os.getcwd() # 查看当前工作目录
os.listdir() #列出当前所有文件
os.chdir('c:/python/machine_learning') # 更改当前工作目录
# 打开文件
f = open(fle_address, 'w+r') # 'r' 只读模式，'a'附加模式，如果没有会创建空文件,'w'写入模式，如果没有会创建，如果有会清空再写入
a=f.read() #一次读取所有内容
print(f.read(10)) #打印10个字节的长度
a=f.readlines()# 一次读取，按照行形成列表
print(f.readline()) #打印1行数据

f.tell() #当前文件流位置
f.seek(3,from) #from可选为:0文件开始 1当前位置 2文件末尾位置

f.write('something')
f.close()
with open('file_address','r') as f:
    f.write('something')
```



* ##### 字符串替换


#在shell中运行python代码
1、菜单栏open，F5
2、exec(open('main_learning.py').read())


#########################  常用函数  #########################
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))

import imp
imp.reload(module) #导入模块之后才可reload
array(range(12)).reshape(3,4) #将一位数组变成二维数组
type(a) # 查看属性

string.title() : First letter upper
string.upper() : 
string.lower() : 
string.rstrip() : delete the blank on the right temporitaly

#随机数用numpy里的random比较好用
random.random(10):输出10个随机数[0，1)
random.random((2,3)):输出array(2,3)形式随机数[0，1)
random.rand(3,2,1) : 输出arrary(3,2,1)形式随机数
random.randn(3,2,1):输出arrary(3,2,1)形式标准正态分布随机数
random.randint(1,10,10):输出10个随机整数[1，10)
random.normal(1,1,10) : 输出10个正态随机数mean=1，sd=1
random.choice(10,4) : 从range(10)里随机取4个数

#数组组合
np.append() #和并一列
np.concatenate((a,b),axis=0)  
np.hstack() 
np.vstack() 

#time
import time
time.asctime() #'Fri Sep 14 22:44:41 2018'
time.localtime() # time.struct_time(tm_year=2018, tm_mon=9, tm_mday=14, tm_hour=14, tm_min=43, tm_sec=11, tm_wday=4, tm_yday=257, tm_isdst=0)
time.strftime('%a-%b-%y')

    %a      本地(local)简化星期名称
    %A      本地完整星期名称
    %b      本地简化月份名称
    %B      本地完整月份名称
    %c      本地相应的日期和时间表示
    %d      一个月中的第几天(01-31)
    %H      一天中的第几个小时(24小时制，00-23)
    %l      一天中的第几个小时(12小时制，01-12)
    %j      一年中的第几天(01-366)
    %m      月份(01-12)
    %M      分钟数(00-59)
    %p      本地am或者pm的相应符
    %S      秒(01-61)
    %U      一年中的星期数(00-53,星期天是一个星期的开始,第一个星期天之前的所有天数都放在第０周)
    %w      一个星期中的第几天(0-6,0是星期天)
    %W      和%U基本相同，不同的是%W以星期一为一个星期的开始
    %x      本地相应日期
    %X      本地相应时间
    %y      去掉世纪的年份(00-99)
    %Y      完整的年份       
    %z      用+HHMM或者-HHMM表示距离格林威治的时区偏移(H代表十进制的小时数，M代表十进制的分钟数)
    %Z      时区的名字(如果不存在为空字符)
    %%      %号本身
            %p只有与%I配合使用才有效果
            当使用strptime()函数时，只有当在这年中的周数和天数被确定的时候%U和%W才会被计算



对于多维列表排序
list_a = [('a',3),('b',4),('c',1)]
sorted(list_a, key=lambda tuple:tuple[2], reverse=True)  #lambda是固定写法，意思是按照元素第二个成分排序

'矩阵操作'
import numpy as np
np.mat.min(0) #求mat数组按列最小值，结果为单行数据
np.mat.max(0) #求mat数组按列最大值，结果为单行数据
a = np.mat([[-1,2],[2,3]])
b = np.mat([[3,4],[4,5]])
print '\n a transpose:\n',a.T #转置
print '\n a inv:\n',np.linalg.inv(a) # 求逆
print '\n a inv:\n',a.I # 求逆
print "\n a-b: \n",a-b  # a - b，矩阵相减
print "\n a dot b: \n",a*b #2x2矩阵，矩阵相乘
print "\n a .dot b: \n",multiply(a,b) #矩阵点乘
print "\n a/b \n:",b/a  # numpy中的除是对矩阵元素展开计算
print "\n a trace：\n",np.trace(a)  #求迹
eigval,eigvec = np.linalg.eig(a) #特征，特征向量
print "求矩阵的行列式"
    print det(lis)


a = np.zeros([4,5])
print  '\n all zero \n',a
a = np.ones([7,6])
print  '\n all one \n',a
a = np.eye(4,7)
print  '\n 4x7 diagonal \n',a
a = np.diag(range(5))
print  '\n 5x5 diagonal \n',a
a = np.empty([2,3])
print '\n empty \n',a

列表：
list.append('text') /add text to last position in list
list.issert(2,'text') /add text to the given postion in list
list.sort() /list's is ordered forever
sorted(list) /temporarily rearrange the list
set(list): eliminate the repetition
list.index(num) #给出num所在的位置
list.pop() #pop出列表最后一个值
list[1:5] #取1，2，3，4 不包括最后一个

元组：
固定的列表，用括号表示

字典：
dict.get(key, default) #查询key对应的值，假如没有则返回默认值default

#对字典进行排序，结果为列表，
# key=operator.itemgetter(0)，是根据key排序，key=operator.itemgetter(1)，是根据value排序
# 默认是升序，reverse = True，是降序排列
for key,value in dic.items():
    print(key:value)


sorted(a.items(),key=operator.itemgetter(0), reverse=False)  
sorted(a.items(),key=lambda tuple:tuple[1],, reverse=False)  

#########################  pandas  #########################
pd.Series([1,2,np.nan,4])
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
s=df.describe() # summary
df1.fillna(value=5)
df1.dropna(how='any')

#########################  管理包  #########################
查询包的位置 package.__file__


单下划线开头：单下划线开头的变量和函数被默认当作内部函数，如果使用 from a_module import * 导入时，
这部分变量和函数不会被导入。如果使用 import a_module 这样导入模块，仍然可以用 a_module._some_var 这样的形式访问。

单下划线结尾：这在解析时并没有特别的含义，但通常用于和 Python 关键词区分开来。

双下划线开头：表示名字改编 (Name Mangling)，即如果Test 类里有一成员 __x，那么 dir(Test) 时会看到 _Test__x 非 __x。
这是为了避免该成员的名称与子类中的名称冲突。

双下划线开头双下划线结尾：Python 官方推荐永远不要将这样的命名方式应用于自己的变量或函数，而是按照文档说明来使用。



for a in list:
	print(a)
	
if a == 'sb':
	print(a)
elif a>='nb':
	pass
else:
	print('sb')
while t:
	break
	continue

def fun():
	text

函数定义，*元组

