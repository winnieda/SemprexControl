from msl.loadlib import Client64

class SAMCClient(Client64):
    def __init__(self):
        super(SAMCClient, self).__init__(module32='semprexcontrol.samc_server')

    def set_addr(self, addr: int, baud: int) -> int:
        """Call SAMC_SetAddr via the server."""
        return self.request32('set_addr', addr, baud)
