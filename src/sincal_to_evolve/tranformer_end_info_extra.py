from typing import Optional

from zepben.evolve import *


class PowerTransformerTankInfo(AssetInfo):
    power_transformer_info: str = None
    """"The power transformer info of this power transformer tank info."""
    # TODO: Add this class to the SDKs


class TransformerTest(IdentifiedObject):
    base_power: int = -9999
    temperature: int = -9999


class ShortCircuitTest(TransformerTest):
    voltage: int = -9999
    power: int = -9999
    current: int = -9999


class NoLoadTest(TransformerTest):
    loss: int = -9999
    excitingCurrent: int = -9999


class TransformerEndInfo(AssetInfo):
    # TODO: Add this class to the SDKs
    ratedS: int = -9999
    ratedU: int = -9999
    endNumber: int = -9999
    emergencyS: int = -9999
    power_transformer_tank_info: Optional[PowerTransformerTankInfo] = None
    short_circuit_test: Optional[ShortCircuitTest] = None
    no_load_test: Optional[NoLoadTest] = None
    connection_kind: WindingConnection = None
    phase_angle_clock: int = -9999


class TransformerStarImpedance(IdentifiedObject):
    r: float = -9999.9
    r0: float = -9999.9
    x: float = -9999.9
    x0: float = -9999.9
    transformer_end_info: Optional[TransformerEndInfo] = None
