#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(BowenRan)s
"""

import numpy as np
import matplotlib.pyplot as plt
plt.subplot2grid((3, 3), (0, 0),colspan = 3)
plt.subplot2grid((3, 3), (1, 0),colspan = 2)
plt.subplot2grid((3, 3), (1, 2),rowspan = 2)
plt.subplot2grid((3, 3), (2, 0))
plt.subplot2grid((3, 3), (2, 1))
plt.show()