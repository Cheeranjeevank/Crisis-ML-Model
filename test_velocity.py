from app.Core.velocity_detector import VelocityDetector

detector = VelocityDetector()

yesterday_entropy = 0.45
today_entropy = 0.60

velocity = detector.calculate_velocity(today_entropy, yesterday_entropy)

print("Yesterday:", yesterday_entropy)
print("Today:", today_entropy)
print("Velocity:", velocity)