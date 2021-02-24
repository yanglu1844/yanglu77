'''
常用的API介绍
八大定位方式：--所有的控件都必须定位到才能进行操作，但每一个控件并非有所有的属性。（右键点击检查 会出现页面代码）
1.通过id定位控件（find_element_by_id）
'''

'''
eg:
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(5)
driver.find_element_by_id("cart_num").click()
'''

'''2.通过name来定位（find_element_by_name）'''
'''
eg:
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(5)
driver.find_element_by_name("key").send_keys('书包')
'''


'''3.通过class_name定位（find_element_by_class_name），html上是class,通过类来定位, 注意如果值带有空格，那么就不建议用class_name 去定位。'''

'''eg:
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(5)
driver.find_element_by_id("kw").send_keys('易烊千玺')
time.sleep(5)
driver.find_element_by_class_name("s_btn").click()
'''

'''4.通过链接定位,find_element_by_link_text(a标签,有href属性）
必须为文字，且可点击可跳转的链接地址。一般是a标签，herf属性 ，并且是一个链接地址，'''
'''eg:
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(5)
driver.find_element_by_link_text("登录").click()
'''

'''5.通过部分链接（部分文本）定位,find_element_by_partial_link_text(a标签,有href属性）
必须为文字，且可点击可跳转的链接地址。一般是a标签，herf属性 ，并且是一个链接地址'''
'''eg:
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(5)
driver.find_element_by_partial_link_text("全场").click()
'''

'''在自动化测试过程中，当一个控件没有’name,id,class,‘’等属性或者用前5种定位方法定位不到的时候， 就需要用到其他的方法。
对于web每一个页面来说是一种dom树形结构，页面中有平级也有多层的分支嵌套关系。以‘家谱图’来做解释说明。当我们要去定位一个在多级关系下的控件，就需要用控件的绝对路径或者相对路径来通过xpath定位到这个控件。'''

'''6.通过xpath路径定位---绝对路径driver.find_element_by_xpath
绝对路径： 从根部找起，往下一层一层找，直到这个控件所在的路径。
          比如我要定位一个 搜索框的。首先要进入网址页面 ，按’ctrl+f’ 在页面的左下方出现输入框 ，在输入框内去写xpath的路径。
          绝对路径以/开始写起,副级与子级用/表示
          注意看查找框 右面的数字显示 如果显示1of1 就代表你所查找的控件是唯一的， 如果不是，那就代表的不是唯一， 需要进一步的用下标表示所查找的控件是第几个， 记住：xpath 的下标从1开始
          在写xpath过程中 如果副级中没有相同的子级路径  可以直接写副级，或者带上副级的下标， 但是，如果副级下面有相同路径的就必须要带上‘下标’，以防止定位错误。
          找到xpath 路径为唯一的，就可以去代码定位
          绝对路径比较复杂过长， 在定位的时候常常比较繁琐， 在正常去定位控件的时候， 一般用相对路径比较多。
相对路径:相对路径 先从某一个为特定属性开始定位 从而再去去定位到你想要定位到的控件。
        相对路径以//开始写起，特定属性对应的标签类型[@属性=属性值]/再去写想要查找的控件的标签。
          Eg://div[@class=’schbox’]/fom/input[1]  先定位到class=’schbox’的控件再去找form 的控件再去找input的第一个控件
        一般相对路径里的特定属性不要用链接地址，action的，method的style的，页面比较多的属性，就不要用。用比较固定的属性。或者控件自身有特定的属性，也可以直接写。
          Eg://div[@class=’nav_bar’]
        又或者控件里面的某一个属性不是唯一的 也可以增加一个来去确定，直到达到唯一
          Eg：//input[@name=’keys’ and @class=’but1’ and @type=’text’] 等等
        如果一个属性的值比较长， 可以用contains来包含属性的内容,内容得是连续的,因为是包含 所以属性跟值之间用 ‘，’
          Eg://input[contains(@placeholder,’关键字’)]  
        定位到某一个控件的上一级， 那就在控件的路径前加上.. 来定位上一级
          Eg://div[@class=’main_bar’][2]/.. 或者 //input[@class=’but1’and @name=’key’]/..
        或者通过正则匹配， 用*代表所有标签类型 直接跟属性和属性值，通过想要找的属性值去定位到控件
          Eg://*[@class=’img’] 只要class的这个属性的属性值是’img’的就是我要找的控件。
        注意当写完xpath ，写代码的时候 注意xpath 内容与代码的 引号 区别 ， 不能同是单引号，或者同是双引号。
'''

'''eg:绝对路径
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://101.133.169.100/yuns/index.php')

time.sleep(3)
driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys('棉服')
'''


'''eg:相对路径
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://101.133.169.100/yuns/index.php')

time.sleep(3)
# driver.find_element_by_xpath("//input[@class='but1']").send_keys('棉服')
driver.find_element_by_xpath("//input[contains(@placeholder,'关键字')]").send_keys('牛奶')
time.sleep(3)
driver.find_element_by_xpath("//*[@class='but2']").click()
time.sleep(3)
'''

'''7.通过CSS 选择器定位 --绝对路径和相对路径
CSS跟xpath定位也有绝对路径和相对路径，但是语法上的书写有所不一样，思想是一致。
CSS绝对路径：通过 > 号来分割层级
Eg: html > body > div > div > div > div > form > input
CSS 的绝对路径简单了解即可，一般只能用绝对路径定位就用xpath'''

'''Css相对路径:
第一种---id属性；如果一个控件有id 属性就可以通过 标签 #属性值
eg:  i#cart_num   #号的意思通过id 来定位'''

'''eg:
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.find_element_by_css_selector("i#cart_num").click()
'''


'''
第二种---class属性； 如果一个控件有class属性 就可以通过 标签 .属性值
eg: input.but1  或div.main_bar  英文的句号 . 意思就是通过class 来定位
如果控件属性不是id ，class的 那就是通过定是标签[属性=属性值]
就是在xpath的相对路径的基础上少了@
Eg: input[name=bar]
对于一个属性对应不了唯一值，xpath 是用and 来增加属性和属性值的， 那CSS 是直接加[属性=属性值]
Eg: div[class=’sch_hidden_bar’][style='key']
CSS 相对路径中最终所定位的不是唯一值时， 则是用标签:nth-child() 去选择第几个， 下标也是从1开始
Eg: div.logo>.sch>.schbox>form>input:nth-child(1)
也可以用:fist-child /last-child--找第一个
Eg:div.log>.sch>.schbox>form>input:last-child---找最后一个
xpath对控件的排序方式是相同的控件排在一起，但是css 不是， 它是混着标签来的；所以在数下标的个数时 要注意下，依次去数所要的控件
比如我要定位的百度里的 ‘百度一下’按钮定位的是 form#form>span:nth-child(9)>input
'''


'''通过tag_name（标签类型）来定位
Eg:driver.find_element_by_tag_name(‘class’) 默认定位到类型的第一个。
但是 一个页面都很多相同的类型， 这种的精确不到具体的控件
所以用driver.find_elements_by_tag_name 找到一个标签类型的所有，存放为列表，在通过下标去具体，但是这种的还是会造成混乱。一般不建议用这个方法去定义
'''



