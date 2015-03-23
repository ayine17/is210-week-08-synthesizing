#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_02, password authentication"""


import authentication
import getpass


INCORRECT = 'Incorrect username or password. You have {} attempts left.'


def login(username, maxattempts=3):
    """implementing the structure of a login or authentication screen
        Args:
            username (str): A string representing the username of the user
                            attempting to log in

            maxattempts (int, optional): An integer represent the maximum number
                                         of prompted attempts before the
                                         function returns False.
        Returns:
        passw (bool):True if the user has successfully authenticated before
                     hitting the maximum number of attempts or False if they
                     exceed that maximum number of failed attempts.

    Examples:
        >>> task_02.login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        Incorrect username or password. You have 2 attempts left.
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False

        >>> task_02.login('veruca', 2)
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        True

    """

    passw = False

    # inputs = raw_input('Please enter your password:')

    while passw is False and maxattempts > 0:
        # inputs = raw_input('Please enter your password:')
        password = getpass.getpass('Please enter your password:')
        # authentication.authenticate(username, password)
        passw = authentication.authenticate(username, password)

        if passw is not False:
            passw = True

        else:
            maxattempts -= 1
            print INCORRECT.format(maxattempts)

    return passw
