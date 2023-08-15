# KWSGalcloud - 使用Alist作为存储的资源站

## 这是什么？
KWSGalcloud是在2022年暑假开始开发的一个资源站，最初是为群友写的。使用Alist作为存储后端(*需要单独安装并配置Alist，然后更改此应用的配置文件config.py从而连接)，前端页面基于AdminLTE制作。
这个项目最初只有最基本的文件浏览和下载功能，现已加入积分系统，管理页面等功能。这个项目是作为Galgame资源站设计的，当然也可以用作其他资源站。您可以在此文件的最后一节看到所有页面的截图，以及他们对应的功能。
## 目前实现的功能
- 基础前端(支持文件夹的文件浏览器，搜索功能，前端页面)
- 用户注册登录
- 用户界面(查看积分购买的资源，用兑换码兑换积分，换头像)
- 管理员界面(管理注册邀请码，添加积分兑换码，封禁用户，查看整体积分使用情况)
- 积分系统(下载资源扣除相应积分，以及下载权限检查)  
□ OnlineGal在线游玩功能-正在开发中
## 如何使用
您需要先确保您已经安装了这些外部依赖：
- Alist (可以不用部署在同一个服务器上)
- mysql
- python
如果您已经准备好了，我们可以开始了：
1. 安装requirements中的依赖
2. 导入mysql,或者按照下面的截图来创建一个数据库
   - ![数据库](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/1c7ec955-3cb5-4894-a758-4c8f28372115)
3. 修改配置文件config.py。在这里面我没有去掉以前调试时使用的数据，您可以直接修改。下面会讲一下这些设置项都是什么意思
   - initial_integral：这是新注册用户系统默认赠送的初始积分。如果您不想给新注册用户一些积分的话，可以把他改成0。
   - app_name：这个是应用的名字，也是网站的标题。
   - app_version：应用的版本
   - secret_key：这个是session用的，可以不用管他
   - redirect_url：这个是重定向url，新版本已经弃用，您可以随意修改。建议修改为您网站的url
   - alist_url：这个是您alist站点的 ```搜索``` url，您只需要修改前半部分的域名就可以
   - alist_home：这个是您alist站点的主页url
   - alist_passwd：如果您的alist分享设有密码，请填写
   - alist_path：如果您并不想把您alist上的根目录作为资源站的根目录，请修改此为您alist上想要共享的目录
  (*此处注意：按照本应用的设计，用户在经过积分扣除和鉴权后浏览器获取的下载地址并非您的alist页面，而是本应用在您alist获取的下载地址。例如，如果您在alist上绑定了onedrive作为存储，那么本应用会直接在用户下载时向您的alist获取onedrive地址并返回给用户的浏览器。所以，您alist站点所统计的下载者ip等信息并非是真正的下载者ip，而是部署此应用的服务器ip)
   - #mysql 部分即为您的数据库设置，您可以按照您的情况自行修改
4. 使用python运行main.py即可启动。您可能需要设置反向代理以使用域名访问
## 文件结构
![文件们](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/3a1d854f-d3c4-4e55-826a-2aca18b72eb7)

## 一些截图
- 在这个部分，您可以看到主要页面的截图。主页内容和宣传板可自定义内容，您可在 ```/templates/home``` 中直接修改
![主页](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/1a6a8b3e-83ec-43b9-99a1-5d8fd16a2c54)
![搜索1](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/0a0dbc74-a048-4017-b46c-5f2e2cadafd0)
![搜索2](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/65a2b235-bcdb-42b3-98a9-ae14dac92b5b)
![管理员面板](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/214dd4cb-bc9d-415c-8944-a44e0fcc4c5b)
![登录](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/87fd1973-cef8-4799-8bc9-836422d12713)
![注册](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/624fad44-c721-4f36-b594-bb9716dec26b)
![用户信息](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/7308bd19-f51f-4607-8fa7-91b6a98e175c)
![用户头像](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/957ba6d8-7d49-4e6a-a2ed-562cc369a0d1)
![用户管理](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/904659ab-03ac-4b33-b688-072bf2c128aa)
![忘记密码](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/30aa397e-ac98-4b39-afb0-05d1087c9bb1)
![所有](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/4a4d4f18-4f2a-4dda-a9e3-4d2e0e912819)
![积分管理](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/67cf02be-8d48-43c3-ac9d-31f09c77be0a)
![积分兑换](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/5a822adc-c182-477e-a447-d69bd6e08397)
![管理员视角](https://github.com/hedgehog-qd/KWSGalcloud/assets/70051464/cb3494fb-9759-43b5-88b7-ff0f416fd0b3)
