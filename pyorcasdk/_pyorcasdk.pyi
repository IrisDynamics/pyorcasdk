"""
Python binding for the C++ orcaSDK
"""
from __future__ import annotations
import typing
__all__ = ['Actuator', 'ForceMode', 'HapticMode', 'KinematicMode', 'MessagePriority', 'MotorMode', 'OrcaError', 'OrcaResultInt16', 'OrcaResultInt32', 'OrcaResultList', 'OrcaResultMotorMode', 'OrcaResultUInt16', 'PositionMode', 'SleepMode', 'StreamData', 'important', 'not_important']
class Actuator:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self, name: str, modbus_server_address: int = 1) -> None:
        ...
    @typing.overload
    def __init__(self, serial_interface: ..., clock: ..., name: str, modbus_server_address: int = 1) -> None:
        ...
    @typing.overload
    def begin_serial_logging(self, log_name: str) -> OrcaError:
        ...
    @typing.overload
    def begin_serial_logging(self, log_name: str, log: ...) -> OrcaError:
        ...
    def clear_errors(self) -> OrcaError:
        ...
    def close_serial_port(self) -> None:
        ...
    def disable_stream(self) -> None:
        ...
    def enable_stream(self) -> None:
        ...
    def get_errors(self) -> OrcaResultUInt16:
        ...
    def get_force_mN(self) -> OrcaResultInt32:
        ...
    def get_mode(self) -> OrcaResultMotorMode:
        ...
    def get_position_um(self) -> OrcaResultInt32:
        ...
    def get_power_W(self) -> OrcaResultUInt16:
        ...
    def get_stream_data(self) -> StreamData:
        ...
    def get_temperature_C(self) -> OrcaResultUInt16:
        ...
    def get_voltage_mV(self) -> OrcaResultUInt16:
        ...
    @typing.overload
    def open_serial_port(self, port_number: int, baud_rate: int = 19200, interframe_delay: int = 2000) -> OrcaError:
        """
        Open serial port using port number
        """
    @typing.overload
    def open_serial_port(self, port_path: str, baud_rate: int = 19200, interframe_delay: int = 2000) -> OrcaError:
        """
        Open serial port using port path
        """
    def read_multiple_registers_blocking(self, reg_start_address: int, num_registers: int, priority: MessagePriority = ...) -> OrcaResultList:
        ...
    def read_register_blocking(self, reg_address: int, priority: MessagePriority = ...) -> OrcaResultUInt16:
        ...
    def read_wide_register_blocking(self, reg_address: int, priority: MessagePriority = ...) -> OrcaResultInt32:
        ...
    def read_write_multiple_registers_blocking(self, read_starting_address: int, read_num_registers: int, write_starting_address: int, write_num_registers: int, write_data: int, priority: MessagePriority = ...) -> OrcaResultList:
        ...
    def run(self) -> None:
        ...
    def set_mode(self, orca_mode: MotorMode) -> OrcaError:
        ...
    def set_streamed_force_mN(self, force: int) -> None:
        ...
    def set_streamed_position_um(self, position: int) -> None:
        ...
    def update_haptic_stream_effects(self, effects: int) -> None:
        ...
    def write_multiple_registers_blocking(self, reg_start_address: int, num_registers: int, write_data: int, priority: MessagePriority = ...) -> OrcaError:
        ...
    def write_register_blocking(self, reg_address: int, write_data: int, priority: MessagePriority = ...) -> OrcaError:
        ...
    def write_wide_register_blocking(self, reg_address: int, write_data: int, priority: MessagePriority = ...) -> OrcaError:
        ...
    @property
    def name(self) -> str:
        ...
class MessagePriority:
    """
    Members:
    
      important
    
      not_important
    """
    __members__: typing.ClassVar[dict[str, MessagePriority]]  # value = {'important': <MessagePriority.important: 0>, 'not_important': <MessagePriority.not_important: 1>}
    important: typing.ClassVar[MessagePriority]  # value = <MessagePriority.important: 0>
    not_important: typing.ClassVar[MessagePriority]  # value = <MessagePriority.not_important: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MotorMode:
    """
    Members:
    
      SleepMode
    
      ForceMode
    
      PositionMode
    
      HapticMode
    
      KinematicMode
    """
    ForceMode: typing.ClassVar[MotorMode]  # value = <MotorMode.ForceMode: 2>
    HapticMode: typing.ClassVar[MotorMode]  # value = <MotorMode.HapticMode: 4>
    KinematicMode: typing.ClassVar[MotorMode]  # value = <MotorMode.KinematicMode: 5>
    PositionMode: typing.ClassVar[MotorMode]  # value = <MotorMode.PositionMode: 3>
    SleepMode: typing.ClassVar[MotorMode]  # value = <MotorMode.SleepMode: 1>
    __members__: typing.ClassVar[dict[str, MotorMode]]  # value = {'SleepMode': <MotorMode.SleepMode: 1>, 'ForceMode': <MotorMode.ForceMode: 2>, 'PositionMode': <MotorMode.PositionMode: 3>, 'HapticMode': <MotorMode.HapticMode: 4>, 'KinematicMode': <MotorMode.KinematicMode: 5>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class OrcaError:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __bool__(self) -> bool:
        ...
    def __init__(self, failure_type: int, error_message: str = '') -> None:
        ...
    def __repr__(self) -> str:
        ...
    def what(self) -> str:
        ...
class OrcaResultInt16:
    error: OrcaError
    value: int
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class OrcaResultInt32:
    error: OrcaError
    value: int
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class OrcaResultList:
    error: OrcaError
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def value(self) -> ...:
        ...
    @value.setter
    def value(self, arg0: ..., std: ...) -> None:
        ...
class OrcaResultMotorMode:
    error: OrcaError
    value: MotorMode
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class OrcaResultUInt16:
    error: OrcaError
    value: int
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StreamData:
    errors: int
    force: int
    position: int
    power: int
    temperature: int
    voltage: int
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
ForceMode: MotorMode  # value = <MotorMode.ForceMode: 2>
HapticMode: MotorMode  # value = <MotorMode.HapticMode: 4>
KinematicMode: MotorMode  # value = <MotorMode.KinematicMode: 5>
PositionMode: MotorMode  # value = <MotorMode.PositionMode: 3>
SleepMode: MotorMode  # value = <MotorMode.SleepMode: 1>
important: MessagePriority  # value = <MessagePriority.important: 0>
not_important: MessagePriority  # value = <MessagePriority.not_important: 1>
