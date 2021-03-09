from tranformer_end_info_extra import *


def DD0(ptei1: TransformerEndInfo, ptei2: TransformerEndInfo):
    ptei1.connection_kind = WindingConnection.D
    ptei1.phase_angle_clock = 0
    ptei2.connection_kind = WindingConnection.D
    return [ptei1, ptei2]


vect_grp_dict = {1: 'DD0', 5: 'YNYN0', 14: 'YND1',
                 2: 'DZ0', 59: 'DYN11', 70: 'DY1', 71: 'Y0', 72: 'YN0', 73: 'D0', 74: 'ZNY1', 75: 'ZNY7',
                 76: 'DDN0'}
# TODO: Add all vector groups to the dictionary
# 3: 'DZN0', 4: 'YNY0', 5: 'YNYN0', 6: 'YY0',
# 7: 'YYN0', 8: 'ZD0', 9: 'ZND0', 10: 'DYN1', 11: 'DZ1', 12: 'DZN1',
# 13: 'YD1', , 15: 'YNZN1', 16: 'YZ1', 17: 'YZN1', 18: 'ZD1',
# 19: 'ZND1', 20: 'ZNYN1', 21: 'ZY1', 22: 'ZYN1', 23: 'DY5',
# 24: DYN5, 25: YD5, 26: YND5, 27: YNZ5, 28: YNZN5, 29: YZ5, 30: YZN5,
#  31: ZNY5, 32: ZNYN5, 33: ZY5, 34: ZYN5, 35: DD6, 36: DZ6, 37: DZN6, 38: YNY6,
#  39: YNYN6, 40: YY6, 41: YYN6, 42: ZD6, 43: ZND6, 44: DY7, 45: DYN7, 46: DZ7, 47: DZN7, 48: YD7,
#  49: YND7, 50: YNZN7, 51: YZ7, 52: YZN7, 53: ZD7, 54: ZND7, 55: ZNYN7, 56: ZY7, 57: ZYN7,
#  58: DY11, 59: DYN11, 60: YD11, 61: YND11, 62: YNZ11, 63: YNZN11, 64: YZ11, 65: YZN11, 66: ZNY11,
#  67: ZNYN11, 68: ZY11, 69: ZYN11, 70: DY1, 71: Y0, 72: YN0, 73: D0, 74: ZNY1, 75: ZNY7, 76: DDN0,
#  77: DND0, 78: DNYN1, 79: DNYN11, 80: YNDN1, 81: YNDN11}

# Mapping SINCAL.TwoWindingTransformer.VectorGroup
# vec_grp_str = vect_grp_dict[row['VecGrp']]
# split_vec_grp = []
# split_vec_grp[:] = vec_grp_str

# connection_dict = {'N': WindingConnection.N, 'D': WindingConnection.D, 'Y': WindingConnection.Y}
