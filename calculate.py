# -*- coding: utf-8 -*-

import random


def var_Get(Reference_Value, Floating_Range, Number_of_Samples):
    max_Range = (100 + Floating_Range) / 100
    min_Range = (100 - Floating_Range) / 100
    max_var = Reference_Value * max_Range
    min_var = Reference_Value * min_Range

    database = []
    i = 1
    while i <= Number_of_Samples:
        Random_number = round(random.uniform(min_var, max_var), 3)
        database.append(Random_number)
        i = i + 1
    item = len(database)
    return database, item
