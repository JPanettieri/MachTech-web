# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import multiprocessing

bind = '0.0.0.0:' + str(5005)
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = '-'
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True
