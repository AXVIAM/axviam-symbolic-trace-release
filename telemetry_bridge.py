

# telemetry_bridge.py :: Simulated Telemetry Stream for Oulēna Runtime

import random
import time

def stream_cell_data(cell_count=6):
    """
    Generator that simulates streaming symbolic data for each battery cell in a pack.
    Each yield represents one breath tick across all cells (rotating).
    """
    cell_index = 0
    while True:
        yield {
            "cell_index": cell_index,
            "psi": round(random.uniform(0.40, 0.65), 3),       # symbolic identity (ψₐ)
            "tension": round(random.uniform(0.50, 0.75), 3),   # curvature tension (∇̃)
            "temperature": round(random.uniform(25.0, 35.0), 2),
            "load": round(random.uniform(0.6, 1.0), 2)
        }
        cell_index = (cell_index + 1) % cell_count
        time.sleep(0.1)