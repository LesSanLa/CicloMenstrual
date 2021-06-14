#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ivan Vladimir Meza Ruiz 2018
# GPL 3.0

import random

def execute(*args):
    var=args[0]
    opts=args[1]
    msg = random.choice(["En términos generales, la toalla sanitaria debe sustituirse cada 4 horas para mantenerte fresca. Recuerda que su función es atrapar la sangre que tu cuerpo está desechando y si permanece largo tiempo en contacto con tu zona íntima, podría favorecer la reproducción de bacterias causantes de infección vaginal", "Si tienes algún tipo de síntoma como picazón, enrojecimiento o molestias, es mejor consultar a tu médico para que te asegures que no se ha generado ninguna infección.", "Envuelve las toallas sanitarias en su mismo envoltorio y desechalas en el cesto de basura o en alguna bolsa exclusiva para este tipo de desecho. Nunca en el WC", ]+opts)
    return 'set_slot {0} "{1}"'.format(var,msg)

