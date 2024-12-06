from msl.loadlib import Server32
from ctypes import c_ubyte, c_uint16, c_int32

class SAMCServer(Server32):
    def __init__(self, host, port):
        super(SAMCServer, self).__init__('C:\\Users\\danie_sj4q2on\\ProgrammingProjects\\semprexcontrol\\src\\samc\\Samc.dll', 'cdll', host, port)

    def set_addr(self, addr: c_ubyte, baud: c_ubyte) -> int:
        """Call SAMC_SetAddr function."""
        return self.lib.SAMC_SetAddr(addr, baud)

    def def_parms(self, axis: c_ubyte, filter_params: list, motion_params: list) -> None:
        """Call SAMC_DefParms function."""
        # Reconstruct ctypes arrays from lists
        filter_array = (c_uint16 * 6)(*filter_params)
        motion_array = (c_int32 * 2)(*motion_params)

        # Call the DLL function
        self.lib.SAMC_DefParms(axis, filter_array, motion_array)
