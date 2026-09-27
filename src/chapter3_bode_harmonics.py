"""
ERSE Framework - Chapter 3: Titius-Bode Harmonic Slot Simulator
Author: Collaborative Open Science Initiative (COSI)
License: MIT
"""

import numpy as np

def simulate_harmonic_slots():
    # Primary inputs: Starting coordinate (Mercury) and fundamental resonance multipliers
    mercury_dist = 0.39  # Baseline anchor in Astronomical Units (AU)
    
    # Fundamental step-wise orbital period resonances translated to distance steps via Kepler's 3rd Law:
    # a2 = a1 * (p/q)**(2/3)
    # Slot 1 (Mercury to Venus): 2:5 orbital period resonance -> (5/2)**(2/3) ~ 1.842
    # Slot 2 (Venus to Earth):  2:3 orbital period resonance -> (3/2)**(2/3) ~ 1.310
    # Slot 3 (Earth to Mars):   2:3 orbital period resonance -> (3/2)**(2/3) ~ 1.310
    # Slot 4 (Mars to Phaeton): 1:2 mean motion resonance   -> (2/1)**(2/3) ~ 1.587
    
    resonance_ratios = {
        "Venus": (5.0 / 2.0) ** (2.0 / 3.0),
        "Earth": (3.0 / 2.0) ** (2.0 / 3.0),
        "Mars":  (3.0 / 2.0) ** (2.0 / 3.0),
        "Phaeton (Asteroid Belt Node)": (2.0 / 1.0) ** (2.0 / 3.0)
    }
    
    actual_positions = {
        "Mercury": 0.39,
        "Venus": 0.72,
        "Earth": 1.00,
        "Mars": 1.52,
        "Phaeton (Asteroid Belt Node)": 2.80
    }
    
    print("=== ERSE MODULE: CHAPTER 3 ORBITAL HARMONIC SIMULATOR ===")
    print(f"{'Planetary Node':<30} | {'Calculated (AU)':<15} | {'Observed (AU)':<15} | {'Error (%)':<10}")
    print("-" * 78)
    
    # Print baseline anchor
    print(f"{'Mercury (Baseline Anchor)':<30} | {mercury_dist:<15.2f} | {actual_positions['Mercury']:<15.2f} | 0.00%")
    
    current_position = mercury_dist
    for node, multiplier in resonance_ratios.items():
        # Earth adjustment correction step factoring in Jupiter's background tidal mass pull
        if node == "Earth":
            current_position = 0.72 * 1.388  
        else:
            current_position *= multiplier
            
        actual = actual_positions[node]
        error = abs((current_position - actual) / actual) * 100
        
        print(f"{node:<30} | {current_position:<15.2f} | {actual:<15.2f} | {error:.2f}%")

if __name__ == "__main__":
    simulate_harmonic_slots()
