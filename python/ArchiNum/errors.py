#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BadSelection(Exception):
    """
    Erreur personnalisée pour indiquer une erreur de sélection.
    """
    def __init__(self, message):
        Exception.__init__(self, message)
        super(BadSelection, self).__init__(message)


class BadFonctionName(Exception):
    """
    Erreur personnalisée pour indiquer une erreur dans le nom de la fonction.
    """
    def __init__(self, message):
        Exception.__init__(self, message)
        super(BadFonctionName, self).__init__(message)
