##运用selenium和apscheduler库完成一个小外挂##

在机缘巧合下，我看到一些python写的游戏外挂(其实十分简单，就是点击屏幕位置)。我也想做一个外挂，去点击浏览器的屏幕，以实现一些功能。

这个小外挂基于python，运用了两个库[selenium](http://www.seleniumhq.org/)和[apscheduler](http://apscheduler.readthedocs.org/en/3.0/)。

其中，selenium是一个很出色的浏览器操作库，可以控制（包括IE在内的很多浏览器），主要是用于网页测试使用。同类型的库也有许多。

apscheduler是一个定时框架，支持python解释器和cron格式。

在这里，我将两个框架结合了一下。目的是完成定时点击某个dom的部件，首先F12看到部件的id、name或者class等，然后生成点击等事件即可。

十分简单，无需赘言。源码[GitHub](https://github.com/brandonxiang/SignIn2Work)
