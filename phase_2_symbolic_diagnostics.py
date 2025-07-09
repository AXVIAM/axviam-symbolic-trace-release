# phase_2_symbolic_diagnostics.py
# AXVIAM :: Symbolic Diagnostics + Healing Phase

from breath_loop import breath_loop
from telemetry_bridge import stream_cell_data
from memory_log import memory_trace
from utils.report_generator import export_csv

def run_symbolic_diagnostics(cycles=30, interval=0.1):
    """
    Run a symbolic healing session on simulated curvature data.
    Records symbolic memory and exports final report to CSV.
    """
    print("Starting AXVIAM symbolic diagnostics...")
    stream = stream_cell_data()
    results = []

    for _ in range(cycles):
        cell_data = next(stream)
        result = breath_loop([cell_data])
        print(f"🧪 Full result object: {result}")

        if result and isinstance(result, dict) and result.get("restored"):
            restored = result["restored"]
            results.append({
                "cell_index": restored.get("cell_index"),
                "status": "Restored",
                "restored_psi": restored.get("restored_psi"),
                "restored_tension": restored.get("restored_tension"),
                "breath_cycle": [result.get("inhaled"), result.get("held"), result.get("exhaled")]
            })
        else:
            print(f"⚠️  Restoration result missing or malformed: {result}")

    # Export healing session report
    report_path = export_csv(results, prefix="symbolic_diagnostics")
    print(f"\n✅ Symbolic healing report saved to:\n{report_path}")

if __name__ == "__main__":
    run_symbolic_diagnostics()
