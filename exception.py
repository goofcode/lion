"""
author: Mookeun Ji, goofcode@gmail.com
"""


class NoSuchDriverException(Exception):
    def __init__(self, message='mode should be either "chrome" or "phantom"'):
        self.message = message


class NoSuchLocateMethodException(Exception):
    def __init__(self, message='by should be "id" or "xpath" or "class"'):
        self.message = message


