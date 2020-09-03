# Flask-Learnning
## CONTENT

### 1. 纯文字微博 *[weibo](https://github.com/gcyangxin/Flask-trainning/tree/master/weibo)*

### 2. 微博v2(redis缓存，celery+redis异步，gunicore gevent高并发,nginx+supervisor部署)*[weibo2](https://github.com/gcyangxin/Flask-trainning/tree/master/weibo2)*

### 3. Restful api *[restful](https://github.com/gcyangxin/Flask-trainning/tree/master/restful)*

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
- log功能
- 404页面重写
- 删改，注销
