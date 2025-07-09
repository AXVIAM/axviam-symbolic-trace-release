

# AXVIAM :: Report Generator for Symbolic Restoration Output

import csv
import datetime
import os


def export_csv(report_data, output_dir="reports", prefix="oulena_report"):
    """
    Export the symbolic healing report to CSV.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{timestamp}.csv"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Cell Index", "Status", "Restored ψₐ", "Restored ∇̃", "Breath Cycle"])

        for entry in report_data:
            writer.writerow([
                entry["cell_index"],
                entry["status"],
                round(entry["restored_psi"], 3),
                round(entry["restored_tension"], 3),
                " → ".join(entry["breath_cycle"]) if entry["breath_cycle"] else "-"
            ])

    return filepath