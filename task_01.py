#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""module named task_01.py"""


def get_matches(players):
    """ a fuction that Process the list of names to produce a new list of unique
        matchups between players stored as a list of tuples.

    args:
        players (list): A list of player names.

    return:
        Return the newly created list of tuples.
    example:
        >>> import task_01
        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]

    """
    teams = []
    matchups = []
    play = ()
    singles_matchups = []
    for index, player in enumerate(players):

        for indx, item in enumerate(players):
            if player is not item:
                play = (players[indx], players[index])

                teams.append(sorted(play))

    counter = 0

    for teama, teamb in teams:
        for item, item1 in teams:

            if teama is not item1 and teamb is not item:
                temp = tuple(sorted(teams[counter]))

        counter += 1
        matchups.append(temp)

    for element in matchups:
        if element not in singles_matchups:
            singles_matchups.append(element)

    return singles_matchups
