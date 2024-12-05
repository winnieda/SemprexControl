from msl.loadlib import Server32

class SAMCServer(Server32):
    def __init__(self, host, port):
        super(SAMCServer, self).__init__('C:\\Users\\danie_sj4q2on\\ProgrammingProjects\\semprexcontrol\\src\\samc\\Samc.dll', 'cdll', host, port)

    def set_addr(self, addr: int, baud: int) -> int:
        """Call SAMC_SetAddr function."""
        return self.lib.SAMC_SetAddr(addr, baud)
