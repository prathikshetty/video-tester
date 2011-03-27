# coding=UTF8
## This file is part of VideoTester
## See http://video-tester.googlecode.com for more information
## Copyright 2011 Iñaki Úcar <i.ucar86@gmail.com>
## This program is published under a GPLv3 license

from VideoTester.config import VTLOG

class Meter:
    def __init__(self):
        self.measures = []
    
    def run(self):
        measures = []
        for measure in self.measures:
            VTLOG.info("- Measuring: " + measure.measure['name'])
            measures.append(measure.calculate())
        return measures

class Measure:
    def __init__(self):
        self.measure = dict()
        self.measure['name'] = None
        self.measure['units'] = None
        self.measure['type'] = None
    
    def calculate(self):
        pass
    
    def __max(self, x, y):
        i = y.index(max(y))
        return [x[i], y[i]]
    
    def __min(self, x, y):
        i = y.index(min(y))
        return [x[i], y[i]]
    
    def __mean(self, y):
        sum = 0
        for x in y:
            sum = sum + x
        return sum / len(y)
    
    def graph(self, x, y):
        self.measure['axes'] = [x, y]
        self.measure['max'] = self.__max(x, y)
        self.measure['min'] = self.__min(x, y)
        self.measure['mean'] = self.__mean(y)