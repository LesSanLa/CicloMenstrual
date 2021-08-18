#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ivan Vladimir Meza Ruiz 2018
# GPL 3.0

import random

def execute(*args):
    var=args[0]
    opts=args[1]
    msg = random.choice(['Has un poco de ejercicio, disminuirá molestias de tu periodo.', "Mantente hidratada."]+opts)
    return 'set_slot {0} "{1}"'.format(var,msg)

