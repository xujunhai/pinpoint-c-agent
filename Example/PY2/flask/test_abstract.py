#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import abc
from pinpoint.plugins.PinpointCommonPlugin import PinpointCommonPlugin


class AllFle():
    all_type='file'
    @PinpointCommonPlugin('AllFle', __name__)
    @abc.abstractmethod
    def read(self):
        pass


class Txt(AllFle):
    @PinpointCommonPlugin('Txt', __name__)
    def read(self):
        return "Reading txt!"
