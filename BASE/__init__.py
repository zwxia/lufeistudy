# -*- coding:utf-8 -*-
import os

BASE_ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE_ROOT)
LOG = os.path.join(ROOT, "log")
print(BASE_ROOT)
print(ROOT)
print(LOG)