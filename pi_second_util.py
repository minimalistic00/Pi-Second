import math
def pi_second(omega):
    """
    Calculate the duration for a phase advance of exactly π radians in uniform harmonic oscillation.
    
    This is a conceptual helper for educational/technical use (not an SI unit). 
    The time (in seconds) is π / ω, where ω is the angular frequency (rad/s).
    
    Args:
        omega (float): Angular frequency in rad/s

    Returns:
        float: Time interval (seconds) for π radians phase advance

    Example:
    
            >>> pi_second(1)  # ω = 1 rad/s
        3.141592653589793
    """
    return math.pi / omega
