#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import gevent.monkey

gevent.monkey.patch_all()




#debug = True
#loglevel = 'debug'
bind = '127.0.0.1:5000'
#pidfile = 'log/gunicorn.pid'
#logfile = 'log/debug.log'
#errorlog = 'log/error.log'
#accesslog = 'log/access.log'

# 启动的进程数
workers = 17
worker_class = 'gevent'

max_requests=100



x_forwarded_for_header = 'X-FORWARDED-FOR'

