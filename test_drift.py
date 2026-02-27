from app.services.baseline_service import BaselineService

baseline = {
    "typing_entropy": 0.3,
    "sleep_entropy": 0.4,
    "movement_entropy": 0.25,
    "screen_entropy": 0.3,
    "total_entropy": 0.35
}

current_entropy = {
    "typing_entropy": 0.6,
    "sleep_entropy": 0.7,
    "movement_entropy": 0.4,
    "screen_entropy": 0.5,
    "total_entropy": 0.65
}

service = BaselineService()
drift = service.calculate_drift(baseline, current_entropy)

print("Drift:", drift)