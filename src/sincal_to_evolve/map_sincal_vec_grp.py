from transformer_end_info_extra import *


# Mapping SINCAL.TwoWindingTransformer.VectorGroup

class VectorGroupMap(object):

    def __init__(self, vec_grp: int, ptei1: TransformerEndInfo, ptei2: TransformerEndInfo = None):
        self.ptei1: TransformerEndInfo = ptei1
        self.ptei2: TransformerEndInfo = ptei2
        self.vec_grp: str = vec_grp
        self.vec_grp_to_end_info()

    def DD0(self):
        self.ptei1.connection_kind = WindingConnection.D
        self.ptei1.phase_angle_clock = 0
        self.ptei2.connection_kind = WindingConnection.D
        self.ptei1.phase_angle_clock = 0

    def YNYN0(self):
        self.ptei1.connection_kind = WindingConnection.Yn
        self.ptei1.phase_angle_clock = 0
        self.ptei2.connection_kind = WindingConnection.Yn
        self.ptei2.phase_angle_clock = 0

    def YND1(self):
        self.ptei1.connection_kind = WindingConnection.Yn
        self.ptei1.phase_angle_clock = 0
        self.ptei2.connection_kind = WindingConnection.D
        self.ptei1.phase_angle_clock = 1

    def YND1(self):
        self.ptei1.connection_kind = WindingConnection.Yn
        self.ptei1.phase_angle_clock = 0
        self.ptei2.connection_kind = WindingConnection.D
        self.ptei1.phase_angle_clock = 1

    def DYN11(self):
        self.ptei1.connection_kind = WindingConnection.D
        self.ptei2.connection_kind = WindingConnection.Yn
        self.ptei1.phase_angle_clock = 1
        self.ptei2.phase_angle_clock = 1

    def DY1(self):
        self.ptei1.connection_kind = WindingConnection.D
        self.ptei1.phase_angle_clock = 0
        self.ptei2.connection_kind = WindingConnection.Y
        self.ptei2.phase_angle_clock = 1

    def Y0(self):
        self.ptei1.connection_kind = WindingConnection.Y
        self.ptei1.phase_angle_clock = 0

    def YN0(self):
        self.ptei1.connection_kind = WindingConnection.Yn
        self.ptei1.phase_angle_clock = 0

    def D0(self):
        self.ptei1.connection_kind = WindingConnection.D
        self.ptei1.phase_angle_clock = 0

    def ZNY1(self):
        self.ptei1.connection_kind = WindingConnection.Zn
        self.ptei1.phase_angle_clock = 0
        self.ptei2.connection_kind = WindingConnection.Y
        self.ptei2.phase_angle_clock = 1

    def ZNY7(self):
        self.ptei1.connection_kind = WindingConnection.Zn
        self.ptei1.phase_angle_clock = 0
        self.ptei2.connection_kind = WindingConnection.Y
        self.ptei2.phase_angle_clock = 7

    def DDN0(self):
        self.ptei1.connection_kind = WindingConnection.D
        self.ptei1.phase_angle_clock = 0
        self.ptei2.connection_kind = WindingConnection.D
        self.ptei2.phase_angle_clock = 0

    def vec_grp_to_end_info(self):
        vec_grp_dict = {1: self.DD0, 5: self.YNYN0, 14: self.YND1, 59: self.DYN11, 70: self.DY1, 71: self.Y0,
                        72: self.YN0, 73: self.D0, 74: self.ZNY1, 75: self.ZNY7,
                        76: self.DDN0}
        vec_grp_dict.get(self.vec_grp)()

    def get_ends_info(self):
        return [self.ptei1, self.ptei2]


# TODO: Add all vector groups to the dictionary. Only VecGrp recorded on the EE Sincal Master db has beed supported
# Vector Group 1: dd0, 2: dz0, 3: dzn0, 4: yny0, 5: ynyn0, 6: yy0, 7: yyn0,
# 8: zd0, 9: znd0, 10: dyn1, 11: dz1, 12: dzn1, 13: yd1, 14: ynd1, 15: ynzn1,
# 16: yz1, 17: yzn1, 18: zd1, 19: znd1, 20: znyn1, 21: zy1, 22: zyn1, 23: dy5,
# 24: dyn5, 25: yd5, 26: ynd5, 27: ynz5, 28: ynzn5, 29: yz5, 30: yzn5, 31: zny5,
# 32: znyn5, 33: zy5, 34: zyn5, 35: dd6, 36: dz6, 37: dzn6, 38: yny6, 39: ynyn6,
# 0: yy6, 41: yyn6, 42: zd6, 43: znd6, 44: dy7, 45: dyn7, 46: dz7, 47: dzn7, 48: yd7,
# 49: ynd7, 50: ynzn7, 51: yz7, 52: yzn7, 53: zd7, 54: znd7, 55: znyn7, 56: zy7, 57: zyn7,
# 58: dy11, 59: dyn11, 60: yd11, 61: ynd11, 62: ynz11, 63: ynzn11, 64: yz11, 65: yzn11,
# 66: zny11, 67: znyn11, 68: zy11, 69: zyn11, 70: dy1, 71: y0, 72: yn0, 73: d0, 74: zny1,
# 75: zny7, 76: ddn0, 77: dnd0, 78: dnyn1, 79: dnyn11, 80: yndn1, 81: yndn11

