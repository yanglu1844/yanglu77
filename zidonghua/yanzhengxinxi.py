'''
特殊的API:自动化测试场景里不光是要定位控件，也需要鼠标，键盘，特殊属性的获取，多窗口等等的定位。所以需要有特殊的API 来支撑我们自动化的步骤。用八大定位方法不能定位的控件，就需要用特殊的API 用于特殊的场景
第一种：获取title信息
比如  要获取页面以外不能获取到的地方的信息，窗口的名字，地址栏以上的信息等。
要先导入 title的方法 title=driver.title  #print(title)
第二种：获取当前页面的url信息
比如要先进入某一个页面，查看我是不是确实在这个页面 ，通过
 url=driver.current_url  print(url)
 '''

'''
eg:
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
title=driver.title
print(title)
driver.find_element_by_link_text("我的订单").click()
url=driver.current_url
print(url)
'''


'''
第三种：控制浏览器的返回，刷新，前进
  driver.refresh()  刷新
  driver.back() 返回
  driver.forward() 前进
'''

'''
eg:
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.find_element_by_link_text("我的订单").click()
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
'''


'''
第四种：对浏览器窗口大小的设置
比如 打开一个页面， 对页面进行窗口大小的设置，使窗口达到想要的大小去查看页面整体的内容是否显示全。
1.窗体最大化
--driver.maximize_window() 方法
2. 固定窗体的尺寸
--- driver.set_window_size(width.height)
'''
'''
eg:
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.set_window_size(500,500)
time.sleep(3)
'''


'''
第五种：动作事件--click,clear,send_keys
click--点击 ，所有的控件都可以点击 包括页面上的固定的文字显示。
clear--清除 ，如果文本框里有内容，可以先清除在添加新的内容
注意，如果原有的文本框内有文字，想在后面追加文字的话，就需要将文本框在定位一次点击（.click()），再send_keys（内容）
send_keys---输入， 往文本框里输入某内容.
Clear 和send_keys是用于输入框的.
'''

'''
eg:
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").send_keys('我想喝')
time.sleep(3)
driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").send_keys('奶茶')
time.sleep(3)
driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").clear()
'''

'''
第六种 属性的获取   注意 先要赋值 才能获取
1. 获取控件的尺寸信息--.size（width，height）
比如获取文本框的尺寸，先定位到文本框
通过用.size 的方法来拿，它会return 新size 以字典的形式输出  通过按照字典的KEY 去取值
'''

'''
eg:
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
size=driver.find_element_by_xpath('//div[@class="small_cart_name"]/span').size
print(size)
print(size['height'])
'''

'''
2.获取控件的文本信息--.text
比如要拿到百度一下页面的‘百度热榜’文本信息做对比
但是图片上的文本信息取不了
'''

'''
eg:
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
text=driver.find_element_by_xpath('//a[@class="hot-title"]/div').text
print(text)
'''

'''
3.获取某一个控件的某一个属性的值.get_attribute(‘属性’)
比如拿一个文本框里的默认信息
'''

'''
eg:
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
sxz=driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").get_attribute('placeholder')
print(sxz)
'''


'''
4.判断输入框是否显示出来 .is_displayed() 返回的数据类型为bool类型
'''


'''
eg:
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
xs=driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").is_displayed()
print(xs)

if xs==True:
    driver.find_element_by_name("key").send_keys('书包')
else:
    driver.find_element_by_name("key").send_keys('奶茶')
 '''


'''
5.获取文本框里回显的值 --get_attribute(‘value’)
就是指 我输入了一个内容， 不能回显成其他的内容.
注意：密码如果是***的，就回显不了。
'''

'''
eg:
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.find_element_by_name("key").send_keys('书包')
zhi=driver.find_element_by_name("key").get_attribute('value')
print(zhi)
'''

'''
第七种 鼠标事件
   模拟鼠标动作-- 比如想要去点页面其中一控件下的某一个控件等等需要用到鼠标移动的
   这种的需要用到Action Chains 这个类，找到这个类所在的路径 导入进去 from selenium .webdriver.common.action_chains import Action_Chains  在这个类中去调用一些方法
1.鼠标移动到某个地方---move_to_element
举例子： 要点击云商城的‘母婴玩具’下的‘营养辅食’控件，就需要先定位到‘母婴玩具’将鼠标移动到‘母婴玩具’的中间，下级菜单才能出来，才可以定位到‘营养辅食’ 
ActionChains类名后的driver参数一般会给到_init方法，  _init 方法 是指初始化到哪个类的方法.perform （）是指实现所有存储的方法。'''

'''eg:
from selenium .webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
kongjian=driver.find_element_by_link_text('男装女装')
ActionChains(driver).move_to_element(kongjian).perform()  #前面括号里的内容是移动到哪的控件
time.sleep(3)
driver.find_element_by_link_text('内衣袜品').click()
time.sleep(3)
'''


'''
2.右击某个控件--context_click().perform()
 ActionChains(driver).context_click(kongjian).perform()
'''

'''eg:
from selenium .webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
kongjian=driver.find_element_by_link_text('男装女装')
ActionChains(driver).context_click(kongjian).perform()
time.sleep(3)
'''

'''3.双击某个控件--double_click().perform()
ActionChains(driver).double_click(kongjian).perform()'''


'''eg:
from selenium .webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
kongjian=driver.find_element_by_link_text('男装女装')
ActionChains(driver).double_click(kongjian).perform()
time.sleep(3)
'''

'''4.拖拽某个控件偏移到某个地方--drag_and_drop_by_offset()
比如携程上的拖拽框进行偏移，首先先定位到这个控件，不断去调试拽到某个位置,或者通过.size的方法去拿尺寸
右--X 左--y '''

'''eg:
from selenium .webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://passport.ctrip.com/user/reg/home')
time.sleep(3)
driver.find_element_by_link_text('同意并继续').click()
time.sleep(3)
size=driver.find_element_by_id('slideCode').size
print(size)
print(size['width'])
kongjian=driver.find_element_by_class_name('cpt-img-double-right-outer')
ActionChains(driver).drag_and_drop_by_offset(kongjian,size['width'],0)
time.sleep(3)
'''

'''5.或者将一个控件拖拽到另外一个控件的位置，需要将两个控件都得定位出来， 使用的方法是
ActionsChains(driver).drag_and_drop(控件1，控件2）
先导入类。导入driver 获取网址，窗口最大化，定位到两个控件并且赋值，然后用方法进行'''


'''第八种 键盘事件：
   在自动化过程中，如何实现模拟键盘上的动作，就需要先导入键盘的类（Keys）调Keys类.方法名来实现键盘动作
from selenium.webdriver.common.keys import Keys
注意 Keys类的方法中所有变量都是大写的，
简单说几种  
Keys.BACK_SPACE 退格
Keys.SPACE  空格
Keys.CONTROL ，（）‘a’or ’v’ or’ x’等 复制、粘贴、剪切、选中等等 这个方法使用时要注意一下思考一下人工操作时的复制，剪切，粘贴的的光标的位置，
4.Keys.ENTER  确认
格式：
  .send_keys(Keys_BACK_SPACE）'''

'''eg:
from selenium .webdriver.common.keys import Keys
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').send_keys('棉')
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').send_keys(Keys.CONTROL,'a')
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').send_keys(Keys.CONTROL,'c')
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').click()
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').send_keys(Keys.CONTROL,'v')
time.sleep(3)
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').send_keys(Keys.BACK_SPACE)
'''



'''
第九种 等待时间
在打开某一个页面，它都需要加载时间， 人工的是可以看出是否能加载出来，但是自动化不能，所以加入等待时间，是有很有必要的，常用的等待时间有3种。
 面试题：在自动化中有几种等待时间， 每一种都是怎样运用的
  先导入time模块，使用模块里的方法
time.sleep（）-- 是指休眠缓冲几秒，让页面有时间去加载出现。在继续往下执行
   可能每次控件的加载时间都不一致 应该以最慢的时间为基准，再加1-2S的冗余时间，这样时间更充足，避免出现加载不出来导致出错。
 面试题. time.sleep 与sleep 方法有什么区别
   两者都是time类的方法，如果导入的是time模块，那就需要在time模块调sleep 的方法， 如果直接导入的time的sleep方法(from time import sleep）
   就直接用这个sleep（）这个方法就行。 time.sleep 是强制等待时间，必须等完所设置的秒数才能执行下一步。
  2.Implicitly _wait() 隐式等待时间
   driver.implicitly_wait（10） 这个是指的是，虽然设置的是等待10秒，但是页面在5秒就出来了，那它就直接执行下一步了，不会非要把这10秒等完， 最大等待的时间是10秒，
   10秒以后加载不出来就报错了。
     优点：Implicitly _wait （）是全局性的， 它会把所有的控件操作后都等待。 但是可以在中间插入另外的等待时间， 那implicitly_wait 就只执行部分。
   缺点：当xpath 的路径在不同的页面里都有，它会以为所需要的页面已经加载出来，从而进行下一步，但有可能是没有加载出来，这样的话整个 代码执行的顺序已经是乱了的。
3.显示等待时间
需要导入3个类
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
From selenium.webdriver.support import expected_conditions as EC
格式：
=WebDriverWait(driver,15,0.5).until_not(EC.presence_of_element_located(By.XAPTH,”//div[@class=’schbox’]/form/input[1]”))) --意思是最大等待15秒 且每隔0.5的
检查一下，直到xpath 的这个控件出现，将这个控件赋值给一个变量， 在给变量.send_keys()
  或者相反的意思until_not 直到某一个空间 没有了 认为跳转成功，这种的精确性不高，但是是跳转了。
面试题 什么时候要加等待时间
跳转或者进入一个新的页面需要加等待时间
在输入内容之前要加等待时间
'''

'''
第十种 多窗口切换
--driver.Switch_to_window()
   打开一个页面，点击某一个控件，它会进入到另外的窗口。就会呈现多窗口，这时候就需要了解
窗口的句柄在哪个页面，才能避免运行错页面。句柄在第一个窗口 那就不能定位第二个窗口里的控件
(driver.window_handles)打印所有的窗体信息。以列表输出
（driver.current_window_handle）打印当前的窗体信息
 确认所在的窗体之后， 切换到想要的窗体
driver.switch_to.window(driver.window_handles[1]), 以所有的窗体信息为基准按照下标去值


driver.close() 关闭焦点所在的当前窗口
 driver.quit() 关闭所有窗体
'''



'''eg:
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
print(driver.current_window_handle)
driver.find_element_by_link_text('男装活动').click()
time.sleep(3)
print(driver.window_handles)
print(driver.current_window_handle)
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').send_keys('棉服')
'''


'''
第十一种 ： 弹出框 alert
  对没办法查看元素的，这种就叫alert
常见的alert有3种
  对于弹出框中需要输入文本怎么处理
  driver.switch_to.alert.send_keys()
   对于弹出框中的文本信息怎么获取
 print（driver.switch_to.alert.text）
 对于弹出框的确认，取消怎么处理
 driver.switch_to.alert.accept() --确认
 driver.switch_to.alert.dismiss()--- 取消
像是一些正向的按钮 都可以用accept() 反向的按钮都可用dismiss()
'''



'''第十二种:截图--全屏图
driver.get_screenshot_as_file(‘文件保存的绝对路径,图片名’)，图片名以png结尾。
 注意alert界面是没有办法用 .get_screenshot_as_file截图， 需要先dismiss或者accept结束到再截图。   alert的界面可以用python自带的PIL去截。
 '''


'''eg:
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('http://101.133.169.100/yuns/index.php')
# time.sleep(3)
# driver.get_screenshot_as_file(r'C:\yanglu\Desktop\编测编学\jietu.png')
'''

'''面试题 no such element  定位不到控件的原因有哪些：
定位方式错误
等待时间不够
多窗口，焦点定位错误
页面有iframe  -- 这种是html下套了一层html页面'''

'''那对于这种html页面嵌了iframe (html)页面，要去定位iframe里 的控件，处理办法是先定位到iframe,在去定位下面的控件。多个iframe 一层一层的去切
   那么如果这个iframe 有id 或者name 属性且属性值不为空，并且是固定的， 就可以直接写属性值
   driver.switch_to.frame()
如果属性不为空且是固定的 那可以通过xpath 定位到这个控件，给这个控件赋值， 再切到这个变量去
当返回iframe的上级时 通过 driver.switch_to.parent_frame()
直接切回最上级 通过 driver.switch_to.default_content()
时间戳普及， 最后三位数字是毫秒。'''



'''第十三种：下拉选择框的处理--select标签
   下拉选择框的处理先要导入select类,在调用某个方法
先定位到下拉选择框且赋值给一个变量
选择选择框里的某个内容--有3种方式
Select(变量).select_by_visible_text(‘’)传页面可见的文本信息。
Select(变量).select_by_index() 用下标去选择
Select(变量).select_by-value() 用值去选择  
 一定是select标签的才能用这三种方式
'''


'''eg:
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
time.sleep(3)
s=driver.find_element_by_id('J_roomCountList')
Select(s).select_by_visible_text('3间')
time.sleep(3)
Select(s).select_by_index(4)
time.sleep(3)
Select(s).select_by_value('6')
'''


'''
 第十四种：时间控件
 普通的时间控件
对时间选择框下的时间做定位往往不太好定位。只能先去定位到时间选择框按照输入框去处理，那就需要
先清除掉时间框里的默认时间
按照对应的格式去写时间，但只能写当天及以后的日期
格式：eh=driver.find_element_by_id(‘’)
       eh.clear()
       Eh.send_keys(‘2021-01-19’)
 特殊时间控件--有readonly属性
有readonly 属性的控件 是send_keys 不进去内容的  对于这种，需要移除readonly属性 再进行send_keys
格式
变量=”document.getElementById(’‘）.removeAttribute(‘readonly’)”
driver.execute_script(变量）#执行了这个才能移除掉readonly
driver.find_element_by_name(‘’).send_keys(‘时间’)
第二种，当控件没有id的时候， 但是有name ,
变量=”document.getElementsByName()[].removeAttribute(‘readonly’)”  注意一定是Elements
driver.execute_script(变量)
driver.find_element_by_name().send_keys()
 第三种， 通过标签来移除
变量
=”document.getElementsByTagName(‘input’)[].removeAttribute(‘readonly’)
driver.execute_script(变量)
'''

'''eg:
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
time.sleep(3)
e=driver.find_element_by_id('HD_CheckIn')
e.clear()
e.send_keys('2021-02-25')
'''


'''第十五种 滚动条
  对于页面最底部的控件 滚动条处理有几种方法
变量
=’document.documentElement.scrollTop=10000’   设置成一个最大值 从上往下滑到 最底部, 设置成0 从下到最顶部。
driver.execute_script(变量)
 滚动到特定的高度
driver.execute_script(“window.scrollTo(0,document.scrollHeight*0.5)”)
滚动到相对的高度
driver.execute_script(“window.scrollBy(0,-200)”) 负数是指的往上滚动， 正值是指往下滚动
滚动到指定的位置
driver.execute_script(“window.scrollTo(0,1500)”)'''


'''eg:滚动到最底部
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
a='document.documentElement.scrollTop=10000'
driver.execute_script(a)
'''

'''滚动到特定的高度'''
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
a='document.documentElement.scrollTop=10000'
driver.execute_script(a)
time.sleep(3)
b='document.documentElement.scrollTop=0'
driver.execute_script(b)
time.sleep(3)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight*0.5)')
time.sleep(3)
driver.execute_script('window.scrollBy(0,-200)')
time.sleep(3)
driver.execute_script('window.scrollTo(0,1500)')
