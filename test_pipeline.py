from app.services.prediction_pipeline import PredictionPipeline

pipeline = PredictionPipeline()

old_baseline = {
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

yesterday_total_entropy = 0.45

result = pipeline.run_prediction(
    old_baseline,
    current_entropy,
    yesterday_total_entropy
)

print(result)