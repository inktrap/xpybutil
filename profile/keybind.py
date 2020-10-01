#!/usr/bin/env python3
import cProfile
import re
from xpybutil.keybind import update_keyboard_mapping
from xpybutil.compat import xproto

# cProfile.run('update_keyboard_mapping(None)')
# e = xproto.MappingNotifyEvent()


class E:
    def __init__(self):
        self.response_type = 34
        self.sequence = 882
        self.request = 1
        self.first_keycode = 66
        self.count = 1
        self.bufsize = 8


cProfile.run("update_keyboard_mapping(E())")
