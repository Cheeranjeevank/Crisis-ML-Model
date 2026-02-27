import math


def normalize(value: float, max_value: float) -> float:
    """
    Convert value into 0–1 range
    """
    if max_value == 0:
        return 0.0

    normalized = value / max_value

    # Ensure it never exceeds 1
    return min(normalized, 1.0)


def calculate_entropy(value: float) -> float:
    """
    Simple entropy proxy using logarithmic scaling.
    Higher variability -> higher entropy.
    """
    return math.log(value + 1)


def calculate_total_entropy(
    typing_entropy: float,
    sleep_entropy: float,
    movement_entropy: float,
    screen_entropy: float
) -> float:
    """
    Combine all entropy values using predefined weights
    """

    TYPING_WEIGHT = 0.25
    SLEEP_WEIGHT = 0.30
    MOVEMENT_WEIGHT = 0.20
    SCREEN_WEIGHT = 0.15

    total = (
        TYPING_WEIGHT * typing_entropy +
        SLEEP_WEIGHT * sleep_entropy +
        MOVEMENT_WEIGHT * movement_entropy +
        SCREEN_WEIGHT * screen_entropy
    )

    return total
    