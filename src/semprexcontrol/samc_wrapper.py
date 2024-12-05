from ctypes import cdll, c_int, c_uint16, c_uint8, c_int32, POINTER, Structure

# Load the 32-bit DLL
samc = cdll.LoadLibrary("src/samc/Samc.dll")

# Define data structures
class TFilter(Structure):
    _fields_ = [("P", c_uint16),
                ("I", c_uint16),
                ("D", c_uint16),
                ("ILm", c_uint16),
                ("Vff", c_uint16),
                ("MaxErr", c_uint16)]

class TMotion(Structure):
    _fields_ = [("MaxVel", c_int32),
                ("MaxAcl", c_int32)]

# Define function prototypes
samc.SAMC_SetAddr.argtypes = [c_uint16, c_uint16]
samc.SAMC_SetAddr.restype = c_int32

samc.SAMC_DefParms.argtypes = [c_uint8, POINTER(TFilter), POINTER(TMotion)]
samc.SAMC_DefParms.restype = None

samc.SAMC_FindRange.argtypes = [c_uint8, c_uint16]
samc.SAMC_FindRange.restype = c_uint8

# Wrapper functions
def set_addr(addr, baud):
    result = samc.SAMC_SetAddr(addr, baud)
    if result == -1:
        raise Exception("Failed to open COM port")
    return result

def define_params(axis, filter_params, motion_params):
    samc.SAMC_DefParms(axis, filter_params, motion_params)

def find_range(axis, border):
    completed = 0
    while not completed:
        completed = samc.SAMC_FindRange(axis, border)
    print("Range successfully defined")
