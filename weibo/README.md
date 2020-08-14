### 纯文字微博

    #### Installation
    ```
    $ git clone https://github.com/Flask-Learnning/weibo.git
    $ cd bluelog
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
