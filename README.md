# Flask-Learnning
## CONTENT

### 1. 纯文字微博 *[weibo](https://github.com/gcyangxin/Flask-trainning/tree/master/weibo)*
#### screenshot
![index](https://img-blog.csdnimg.cn/2020081518221037.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2djeWFuZ3hpbg==,size_16,color_FFFFFF,t_70)
![profile](https://img-blog.csdnimg.cn/20200815182503697.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2djeWFuZ3hpbg==,size_16,color_FFFFFF,t_70)
#### Installation
```
$ git clone https://github.com/gcyangxin/Flask-trainning.git
$ cd weibo
```
#### dependency
```
$ virtualenv env # for Python2 on Linux & macOS
$ source env/bin/activate
$ pip install -r requirements.txt
```
#### config
```
$ gedit myapp/config.py
`SECRET_KEY=your key`
`SQLALCHEMY_DATABASE_URI=your uri`
```
#### managerdB
```
python manager.py schema_create #createTables
```
#### run
```python run.py```
#### 可改进
- 邮件功能
- log功能
- 404页面重写
- 删改，注销
