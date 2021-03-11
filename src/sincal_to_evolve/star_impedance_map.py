from numpy import sqrt

from sincal_model import *


class TransformerStarImpedanceMap:

    def __init__(self, twt: TwoWindingTransformer):
        self.star_impedance = TransformerStarImpedance()
        self.twt: TwoWindingTransformer = twt
        self.star_impedance.r = twt.un1 ** 2 * twt.ur / (twt.sn * 100)
        self.star_impedance.x = twt.un1 ** 2 * sqrt(twt.uk ** 2 - twt.ur ** 2) / (twt.sn * 100)
        self.star_impedance.r0 = self.sincal_to_zero_sequence()[0]
        self.star_impedance.x0 = self.sincal_to_zero_sequence()[1]

    def r0_x0(self):
        r0 = self.twt.r0
        x0 = self.twt.x0
        return [r0, x0]

    def z0_z1_r0_x0(self, z0_z1, r0_x0):
        z1 = sqrt(self.star_impedance.r ** 2 + self.star_impedance.r ** 2)
        z0 = z0_z1 * z1
        x0 = z0 / sqrt(1+r0_x0)
        r0 = r0_x0*x0
        return [r0, x0]

    def r0_r1_x0_x1(self):
        r0 = self.twt.r0_r1 * self.star_impedance.r
        x0 = self.twt.x0_x1 * self.star_impedance.x
        return [r0, x0]

    def zabnl_zbanl_zabsc(self):
        # TODO: Support this case
        raise RuntimeError("Unsupported flag_z0_input")

    def sincal_to_zero_sequence(self):
        flag_z0_input_switcher = {1: self.z0_z1_r0_x0, 2: self.r0_x0, 3: self.r0_r1_x0_x1,
                                  4: self.zabnl_zbanl_zabsc}
        return flag_z0_input_switcher.get(self.twt.flag_z0_input)()
