from app.services.risk_service import RiskService
from app.Core.velocity_detector import VelocityDetector
from app.services.forecast_service import ForecastService

# Simulated drift
drift = {
    "typing_entropy": 0.6,
    "sleep_entropy": 0.7,
    "movement_entropy": 0.3,
    "screen_entropy": 0.4,
    "total_entropy": 0.65
}

# Yesterday vs Today entropy
yesterday_entropy = 0.45
today_entropy = 0.65

risk_service = RiskService()
velocity_detector = VelocityDetector()
forecast_service = ForecastService()

risk_score = risk_service.calculate_risk_score(drift)
velocity = velocity_detector.calculate_velocity(today_entropy, yesterday_entropy)

forecast = forecast_service.generate_forecast(risk_score, velocity, drift)

print("Risk Score:", risk_score)
print("Velocity:", velocity)
print("Forecast:", forecast)