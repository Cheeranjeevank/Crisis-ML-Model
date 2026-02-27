from app.services.risk_service import RiskService

# Simulated drift values
drift = {
    "typing_entropy": 0.5,
    "sleep_entropy": 0.4,
    "movement_entropy": 0.2,
    "screen_entropy": 0.3,
    "total_entropy": 0.45
}

service = RiskService()

score = service.calculate_risk_score(drift)
level = service.classify_risk(score)

print("Risk Score:", score)
print("Risk Level:", level)