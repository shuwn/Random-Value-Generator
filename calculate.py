# -*- coding: utf-8 -*-

import random

from createnewwindow import CreateNewWindow


def var_Get(Reference_Value, Number_of_Samples, Floating_Range):
    if len(Reference_Value) == 0 or len(Number_of_Samples) == 0 or len(Floating_Range) == 0:
        CreateNewWindow.warningWin("Please enter a values.")
    elif Number_of_Samples.isdigit() == False:
        CreateNewWindow.warningWin("Please enter an integer\n for the Number of Samples.")
    else:
        Reference_Value = float(Reference_Value)
        Number_of_Samples = int(Number_of_Samples)
        Floating_Range = float(Floating_Range)
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
