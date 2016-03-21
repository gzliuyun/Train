2015-12-27  姚永强	10:22am
创建了工程文件夹,写了七个page的url和响应函数的映射(姚永强)

2015-12-28  刘赟  10.42am
创建了个templates文件夹，把与界面相关的html,js,css等文件放进去,但是服务器带的IE浏览器版本太低，支持bootstrap效果不好，所以要看效果复制到自己电脑上看

2015-12-28 刘赟  23.39pm
在template中添加了个人信息和密码管理界面的内容

2015-12-29 9:21 刘昊岩
重新建立了工程（project）web_project，在该工程下建立了应用（app）web_ticket。
将templates文件夹移动到了settings.py所在目录中，在settings.py中添加了数据库和templates的配置信息。
在model.py中构建了模型信息uer和ticket。
把强哥写的url中的匹配加了$，做成绝对匹配。

2015-12-29 16:58 刘昊岩
完成了模型编写model.py，并生成了数据表。本机装了mysql workbench(C:\Program Files (x86)\MySQL\MySQL Workbench 6.1 CE\MySQLWorkbench.exe)，大家可以进去看一下。数据表中有很多是django自带属性生成的，我们自定义的有五个web_ticket_users, web_ticket_ticketinfo, web_ticket_ticketcounts, web_ticket_orders, web_ticket_userorders。具体字段详见数据库或model.py，写文档时记得问我要数据词典。

2015-12-31  姚永强	10:12am
在template中加入了几个新的html页面，分别表示购票及查询余票等功能。但是，查询用户现有订单的页面主要是配合后台数据库，后台的信息render回来之后就可以很轻松的写完这个页面。

2015-12-31 11:46 刘昊岩
添加forms.py，为页面中的每一个表单建一个类，完成views里面注册和登陆的编写。

2016-01-03 00:54 刘昊岩
views.py forms.py models.py全部写完，urls.py有改动