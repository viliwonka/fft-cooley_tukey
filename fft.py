__author__ = 'Vili Volcini'

#library for complex numbers
import cmath
import numpy


class FFT_Transform:

    def __init__(self, samplesSize):

        self.samplesSize = samplesSize

    def Transform(self, vector):

        if len(vector) != self.samplesSize:
            raise Exception("vector size is not equal to sampleSize defined in FFT_Transform")


        pass