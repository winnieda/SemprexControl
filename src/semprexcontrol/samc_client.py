from msl.loadlib import Client64
from ctypes import c_ubyte, c_uint16

class SAMCClient(Client64):
    def __init__(self):
        super(SAMCClient, self).__init__(module32='semprexcontrol.samc_server')

    def set_addr(self, addr: c_ubyte, baud: c_ubyte) -> int:
        """Call SAMC_SetAddr via the server."""
        return self.request32('set_addr', addr, baud)

    def def_parms(self, axis: c_ubyte, filter_params: list, motion_params: list) -> None:
        """Call SAMC_DefParms via the server."""
        assert len(filter_params) == 6, "filter_params must have 6 elements."
        assert len(motion_params) == 2, "motion_params must have 2 elements."
        self.request32('def_parms', axis, filter_params, motion_params)

    def find_range(self, axis: c_ubyte, border: c_uint16) -> bool:
        """Call SAMC_FindRange via the server."""
        return self.request32('find_range', axis, border)

    def reset(self) -> None:
        """Call SAMC_Reset via the server."""
        self.request32('reset')
