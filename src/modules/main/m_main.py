# -*- coding: utf-8 -*-


from specific_classes.pictures import Pictures


class Model(object):

    def __init__(self, config):
        self.pictures = Pictures(config=config)
