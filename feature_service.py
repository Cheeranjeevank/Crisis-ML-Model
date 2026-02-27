from app.core.entropy_calculator import normalize


def process_features(raw_data: dict) -> dict:
    """
    Clean and normalize raw input data.
    """

    typing_raw = raw_data.get("typing_variance", 0)
    sleep_raw = raw_data.get("sleep_variation", 0)
    movement_raw = raw_data.get("movement_deviation", 0)
    screen_raw = raw_data.get("screen_frequency", 0)

    typing_processed = normalize(typing_raw, 1)
    sleep_processed = normalize(sleep_raw, 5)
    movement_processed = normalize(movement_raw, 1)
    screen_processed = normalize(screen_raw, 100)

    return {
        "typing_processed": typing_processed,
        "sleep_processed": sleep_processed,
        "movement_processed": movement_processed,
        "screen_processed": screen_processed
    }