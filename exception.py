"""
author: Mookeun Ji, goofcode@gmail.com
"""


class NoSuchDriverException(Exception):
    def __init__(self, message):
        self.message = message

