from sincal_to_evolve.sincal_to_evolve import ZeroPhaseSequenceInputData
from cim_extra import *
from numpy import sqrt


class TransformerStarImpedanceMap:

    def __init__(self, zero_impedance_input_data: ZeroPhaseSequenceInputData,
                 tei: TransformerEndInfo,
                 sct: ShortCircuitTest, nlt: NoLoadTest):
        self.tei: TransformerEndInfo = tei
        self.sct: ShortCircuitTest = sct
        self.nlt: NoLoadTest = nlt
        self.zero_impedance_input_data: ZeroPhaseSequenceInputData = zero_impedance_input_data
        self.star_impedance = TransformerStarImpedance()

    def get_r_x(self):
        ur = self.sct.power / (self.sct.current * self.tei.ratedU)
        self.star_impedance.r = self.tei.ratedU ** 2 * ur / (self.tei.ratedS * 100)
        self.star_impedance.x = self.tei.ratedU ** 2 * sqrt(self.sct.voltage ** 2 - ur ** 2) / (self.tei.ratedS * 100)

    def z0_z1_r0_x0(self, z0_z1, r0_x0):
        tsi = TransformerStarImpedance()
        # tsi.r =
        # tsi.x =
        # tsi.r0 =
        # tsi.x0 =
        pass

    def r0_x0(self):
        # TODO
        pass

    def r0_r1_x0_x1(self):
        # TODO
        pass

    def zabnl_zbanl_zabsc(self):
        # TODO
        pass

    def input_data_to_star_impedance(self):
        flag_z0_input_switcher = {1: self.z0_z1_r0_x0, 2: self.r0_x0, 3: self.r0_r1_x0_x1, 4: self.zabnl_zbanl_zabsc}
        flag_z0_input_switcher.get(self.zero_impedance_input_data.flag_z0_input)
