#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "20727893"))
    API_HASH = os.environ.get("API_HASH", "d20ab465d7a0546a712b863d36176d76")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6643289556")
