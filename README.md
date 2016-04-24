##运用selenium和apscheduler库完成一个小外挂##

> github源码在此，记得点星:
https://github.com/brandonxiang/selenium_apscheduler_example

****

##引言
机缘巧合，我看到一些python写的游戏外挂的教程（主要是网页游戏），也就是，点击屏幕位置。这也激发了我去实现类似的功能，主要用途是去定期点击浏览器屏幕上的某个控件去实现一些功能。当然这类似的工具还可以应用到其他地方，让人脑洞大开，例如火车抢票，定时打卡之类，内容有点敏感，就不再展开。

##原理

这个小外挂基于python，运用了两个库[selenium](http://www.seleniumhq.org/)和[apscheduler](http://apscheduler.readthedocs.org/en/3.0/)。

其中，selenium是一个出色的浏览器操作库，英文叫做**Web Driver**，主要是用于控制（包括IE在内的）浏览器，网页测试。当然他也可以用作爬虫，参考[我的爬虫之路 (静态+动态JS加载) selenium + PhantomJS](www.jianshu.com/p/5ee55a306dcb)，虽然我觉得爬虫用`request+beautifulsoap`会在效率上更好，因为它不经过浏览器端。同类型的**Web Driver**库还有许多，不在这里展开。

然而，apscheduler是一个定时框架，支持python解释器和cron格式。

##用法

克隆源码，安装第三方库，运行脚本即可。

```
git clone https://github.com/brandonxiang/selenium_apscheduler_example.git
pip install -r requirements.txt
```

##源码

####selenium

引用webdriver获取浏览器，webdriver提供了Firefox，PhantomJS等多款国外浏览器可选。`browser.get()`则是跳转到某个网页。

```
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("http://XX.XX.com/")
```

`find_element_by_id`和`find_element_by_tag_name`则是通过`id`或者`tag_name`去找到对应的元素。`send_keys()`则是往控件内部传值。`click()`则是点击事件。

```
WebDriverWait(browser,10).until(EC.title_contains("系统".decode('utf8')))
```

当网页发生跳转，需要利用`WebDriverWait(browser,时间)`等待，否则页面加载不完整。然而，`until(EC.title_contains("系统".decode('utf8')))`则是等到直到**title**出现**系统**两个字。详细教程参考[selenium官网](www.seleniumhq.org/)

####apscheduler

通过`BackgroundScheduler()`生成一个后台定时框架，然后将其启动。

```
schedular = BackgroundScheduler()
schedular.start()
```

运用解释器去设置时间间隔，这里使用cron，`day_of_week`是一个星期中的某几天或星期几，`hour`和`minute`就是时和分，当然，也有秒的设定。你也可以不使用解释器和cron来设置时间，那样自由度更高。详细教程参考[apscheduler文档](http://apscheduler.readthedocs.org/en/3.0/)

```
@schedular.scheduled_job('cron',day_of_week='mon-fri',hour=8,minute=58)
```

##总结

这里将两个框架结合了一下。总结一下，首先了解控件的对应的id或者class等属性，然后针对某个控件通过属性进行捕获，最后生成**点击，文本输入，页面跳转**等事件即可。