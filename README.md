# Pi-Second
The Pi second is defined as the duration required for the phase of uniform harmonic oscillation to advance by exactly Pi radians.

# π-Second Utility: Conceptual Helper for Phase Duration in Harmonic Oscillation

This Python utility calculates the time interval required for a phase advance of exactly π radians in uniform harmonic oscillation (e.g., simple harmonic motion). 

⚠️ **NOT an official SI unit** — this is a teaching/conceptual tool *only*. There is no "Pi second" in SI units. Use cases include physics education, signal processing, and quantum computing simulations.

---

## Why use this?
- Clarifies the relationship between phase shifts and time in harmonic systems
- Prevents confusion with real units (e.g., `π`-radian intervals depend on angular frequency `ω`)
- Works in any Python environment (VS Code, Jupyter, etc.)

---

## Installation
1. Create a new file `pi_second_util.py` in your project directory with the code below
2. **No extra dependencies** — works with standard Python

```python
import math

def pi_second(omega):
    """
    Calculate time for π radians phase advance.
    
    Args:
        omega (float): Angular frequency (rad/s)
    
    Returns:
        float: Time interval (seconds)
    
    Example:
        >>> pi_second(2 * math.pi * 100)  # 100 Hz oscillator
        0.005
    """
    return math.pi / omega
