class TransformerStarImpedanceMap:

    def __init__(self, flag_z0_input):
        self.flag_z0_input: int = flag_z0_input

    def z0_z1_r0_x0(self):
        # TODO
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

    flag_z0_input_switcher = {1: z0_z1_r0_x0, 2: r0_x0, 3: r0_r1_x0_x1, 4: zabnl_zbanl_zabsc}
