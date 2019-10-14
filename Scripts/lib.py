#!/usr/bin/env python3
# -----------------------------------------------------------------------
# A small python script to scrape the public pastebin archive.
# Copyright (C) 2019  Mili
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------

import os
import socket
import requests
from random import choice

def PrintSuccess(Msg):
    if os.name == 'nt':
        print('[+] ' + Msg)
    else:
        print('\033[1;32m[+]\033[1;m ' + Msg)

def PrintStatus(Msg):
    if os.name == 'nt':
        print('[*] ' + Msg)
    else:
        print('\033[1;34m[*]\033[1;m ' + Msg)

def PrintFailure(Msg):
    if os.name == 'nt':
        print('[-] ' + Msg)
    else:
        print('\033[1;31m[-]\033[1;m ' + Msg)

def PrintError(Msg):
    if os.name == 'nt':
        print('[!] ' + Msg)
    else:
        print('\033[1;31m[!]\033[1;m ' + Msg)

def PrintFatal(Msg):
    if os.name == 'nt':
        print('[$] ' + Msg)
    else:
        print('\033[1;33m[!]\033[1;m ' + Msg)

def IsIPAddress(Address):
    try:
        socket.inet_aton(Address)
        return True
    except socket.error:
        return False

def RandomHeaders():
    return { 'User-Agent': choice(user_agents), 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' }
