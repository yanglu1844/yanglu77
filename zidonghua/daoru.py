#导入
from zidonghua import jichuzhishi as a
import importlib  #加个这个
mymomey=a.shuihou(10000)
print(mymomey)
importlib.reload(a)   #在输出一次

mymomey=a.shuihou(12000)
print(mymomey)

mymomey=a.shuihou(19000)
print(mymomey)

