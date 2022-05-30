manage.py ----- Django项目里面的工具，通过它可以调用django shell和数据库，启动关闭项目与项目交互等，不管你将框架分了几个文件，必然有一个启动文件，其实他们本身就是一个文件。
settings.py ---- 包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量。
urls.py ----- 负责把URL模式映射到应用程序。
wsgi.py ---- runserver命令就使用wsgiref模块做简单的web server，后面会看到renserver命令，所有与socket相关的内容都在这个文件里面了，目前不需要关注它。

## MVC和MTV框架
eb服务器开发领域里著名的MVC模式，所谓MVC就是把Web应用分为模型(M)，控制器(C)和视图(V)三层，他们之间以一种插件式的、松耦合的方式连接在一起，模型负责业务对象与数据库的映射(ORM)，视图负责与用户的交互(页面)，控制器接受用户的输入调用模型和视图完成用户的请求

Django的MTV模式本质上和MVC是一样的，也是为了各组件间保持松耦合关系，只是定义上有些许不同，Django的MTV分别是值：

M 代表模型（Model）： 负责业务对象和数据库的关系映射(ORM)。
T 代表模板 (Template)：负责如何把页面展示给用户(html)。
V 代表视图（View）：   负责业务逻辑，并在适当时候调用Model和Template。

## 在mysite目录下创建应用
> python manage.py startapp blog   #通过执行manage.py文件来创建应用，执行这句话一定要注意，你应该在这个manage.py的文件所在目录下执行
> python manage.py startapp blog2  #每个应用都有自己的目录，每个应用的目录下都有自己的views.py视图

models.py ：之前我们写的那个名为model的文件就是创建表用的，这个文件就是存放与该app(应用)相关的表结构的
views.py  ：存放与该app相关的视图函数的

## 启动django项目
> python manage.py runserver 8080   # python manage.py runserver 
