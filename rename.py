# -*- coding: utf-8 -*-  

import glob
import os

for filename in glob.glob(r'??.py'):
    os.rename(filename, '0%s' % filename)