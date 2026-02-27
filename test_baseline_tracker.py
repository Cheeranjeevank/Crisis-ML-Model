import sys
import os

# Force Backend folder as root
sys.path.append(os.path.abspath("."))

from app.Core.baseline_tracker import BaselineTracker

tracker = BaselineTracker(alpha=0.1)

old_baseline = {
    "typing_entropy": 0.3,
    "sleep_entropy": 0.4,
    "movement_entropy": 0.25,
    "screen_entropy": 0.3,
    "total_entropy": 0.35
}

today_entropy = {
    "typing_entropy": 0.5,
    "sleep_entropy": 0.6,
    "movement_entropy": 0.3,
    "screen_entropy": 0.4,
    "total_entropy": 0.5
}

new_baseline = tracker.update_baseline(old_baseline, today_entropy)

print("Updated Baseline:")
print(new_baseline)