from app.core.entropy_calculator import (
    calculate_entropy,
    calculate_total_entropy
)


def compute_entropy(processed_features: dict) -> dict:
    """
    Convert normalized features into entropy values.
    """

    # Individual entropy values
    typing_entropy = calculate_entropy(
        processed_features["typing_processed"]
    )

    sleep_entropy = calculate_entropy(
        processed_features["sleep_processed"]
    )

    movement_entropy = calculate_entropy(
        processed_features["movement_processed"]
    )

    screen_entropy = calculate_entropy(
        processed_features["screen_processed"]
    )

    # Combined total entropy
    total_entropy = calculate_total_entropy(
        typing_entropy,
        sleep_entropy,
        movement_entropy,
        screen_entropy
    )

    return {
        "typing_entropy": typing_entropy,
        "sleep_entropy": sleep_entropy,
        "movement_entropy": movement_entropy,
        "screen_entropy": screen_entropy,
        "total_entropy": total_entropy
    }