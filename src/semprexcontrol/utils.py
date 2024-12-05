def validate_com_port(port):
    """Ensure COM port is within valid range."""
    if not (1 <= port <= 8):
        raise ValueError("COM port must be between 1 and 8.")

def validate_axis(axis):
    """Ensure axis is within valid range."""
    if not (1 <= axis <= 4):
        raise ValueError("Axis must be between 1 and 4.")
