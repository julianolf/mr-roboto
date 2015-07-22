# -*- coding: utf-8 -*-
"""
    excuses
"""
from irc3 import plugin
from irc3.plugins.command import command
import asyncio
import aiohttp


@plugin
class Excuses(object):
    """
    Commands that prints Programmer Excuses
    """

    def __init__(self, bot):
        self.bot = bot

    @command(permission='view')
    @asyncio.coroutine
    def excuse(self, mask, target, args):
        """
            Excuse

            %%excuse
        """
        request = yield from aiohttp.request('GET', 'https://api.githunt.io/programmingexcuses')
        return (yield from request.text())
