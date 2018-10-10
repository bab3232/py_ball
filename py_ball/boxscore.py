#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:36:55 2018

@author: patrickmcfarlane

boxscore.py contains the BoxScore class that
enables API calls for boxscore related endpoints
"""

from __init__ import api_call, parse_api_call

class BoxScore:
    """ The BoxScore class contains all resources needed to use the boxscore-
    related API calls. stats.nba.com has the following boxscore-related
    API endpoints:
        - boxscoreadvancedv2: Game boxscore containing several advanced
        statistcs
        - boxscorefourfactorsv2: Game boxscore containing statistics related
        to the Four Factors, for team and opponent
        - boxscoremiscv2: Game boxscore containing points scored by type
        of change (paint, fastbreak, etc.) for team and opponent
        - boxscoreplayertrackv2: Game boxscore containing aggregated player
        tracking statistics
        - boxscorescoringv2: Game boxscore containing percentage scoring
        statistics broken down by shot type.
        - boxscoresummaryv2: Game boxscore containing a summary of a
        particular matchup (including game metadata and results)
        - boxscoretraditionalv2: Game boxscore containing basic statistics
        - boxscoreusagev2: Game boxscore containing usage statistics
        and percentage

    The BoxScore class has the following required parameters:

        @param game_id (GameID in the API): 10-digit string that represents
        a unique game. The format is two leading zeroes, followed by a
        '2', then the trailing digits of the season in which the game
        took place (e.g. '17' for the 2017-18 season). The following
        5 digits increment from '00001' in order as the season progresses.
        For example, '0021600001' is the GameID of the first game of the
        2016-17 NBA season.

        @param range_type (RangeType in the API): RangeType controls the
        type of boxscore that is returned. If using the StartPeriod and
        EndPeriod parameters (defined below), RangeType should have a value
        of '0' (DNP players included) or '1' (DNP players excluded). With
        a RangeType value of '2', the StartRange and EndRange values can be
        used to return a boxscore from a customized subset of the given game.

        @param start_period (StartPeriod in the API): String of an integer
        that corresponds to the period for which the boxscore begins.

        @param end_period (EndPeriod in the API): String of an integer that
        corresponds to the period for which the boxscore ends (Overtime
        increments logically, e.g. '5' is the first overtime period).

        @param start_range (StartRange in the API): String of an integer
        that corresponds to the tenths of seconds that have elapsed in the
        game for which the boxscore begins. Valid when RangeType='2'.

        @param end_range (EndRange in the API): String of an integer
        that corresponds to the tenths of seconds that have elapsed in the
        game for which the boxscore ends. Valid when RangeType='2'.
        
    Attributes:

        api_resp: JSON object of the API response. The API response
        has three keys. The 'resource' key describes the type of
        response returned ('boxscore' in this instance). The 'parameters'
        key describes the parameters provided in the API call. The
        'resultSets' key contains the data returned in the API call.

        data: A dictionary of response names. Each response name is a
        key to a list of dictionaries containing the corresponding data.
    """

    def __init__(self, game_id, endpoint='boxscoreadvancedv2',
                 range_type='1', start_period='0', end_period='10',
                 start_range='0', end_range='0'):

        # Controlling the parameters depending on the endpoint
        if endpoint in ['boxscoreplayertrackv2', 'boxscoresummaryv2']:
            params = {'GameID': game_id}
        else:
            params = {'GameID': game_id,
                      'RangeType': range_type,
                      'StartPeriod': start_period,
                      'EndPeriod': end_period,
                      'StartRange': start_range,
                      'EndRange': end_range}

        self.api_resp = api_call(endpoint=endpoint,
                                 params=params)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)
                