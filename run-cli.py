#!/usr/bin/env python
# -*- coding: utf-8 -*-

import herostuff.modules

try:
    herostuff.modules.cli.help()
    herostuff.modules.cli.shell()
except EOFError:
    pass
print("The End Is Nigh!")

