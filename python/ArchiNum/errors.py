# -*- coding: utf-8 -*-

class BadTag(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
        super(BadTag, self).__init__(message)

class BadSelection(Exception):
     def __init__(self, message):
        Exception.__init__(self, message)
        super(BadSelection, self).__init__(message)
