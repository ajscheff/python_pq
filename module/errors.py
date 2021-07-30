#!/usr/bin/env python3

from .colors import colors


class EmptyQueueException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(colors.RED + self.message + colors.ENDC)
