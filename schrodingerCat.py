import random

class QuantumCat:
    def __init__(self):
        # Before observation, the state is uncollapsed (Superposition)
        self.is_observed = False
        self._state = None

    def look_inside_box(self):
        """Opening the box triggers state collapse."""
        if not self.is_observed:
            # The act of observing forces a random collapse to 0 (Alive) or 1 (Dead)
            self._state = random.choice(["ALIVE 😺", "DEAD 🪦"])
            self.is_observed = True
        return self._state

    @property
    def current_state(self):
        if not self.is_observed:
            return "SUPERPOSITION: Simultaneously Alive (50%) and Dead (50%)"
        return f"COLLAPSED: The cat is definitely {self._state}"

# Usage
cat = QuantumCat()

# Phase 1: Sealed Box
print("1. Status before opening:", cat.current_state)

# Phase 2: Open Box
print("2. Opening the box to observe:", cat.look_inside_box())

# Phase 3: Status after opening
print("3. Status after opening:", cat.current_state)