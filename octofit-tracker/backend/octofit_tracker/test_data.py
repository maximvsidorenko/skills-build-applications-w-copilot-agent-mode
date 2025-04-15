# Test data for the OctoFit Tracker app

def get_test_data():
    return {
        "users": [
            {"username": "john_doe", "email": "john@example.com", "password": "password123"},
            {"username": "jane_doe", "email": "jane@example.com", "password": "password123"}
        ],
        "teams": [
            {"name": "Team Alpha", "description": "The first team"},
            {"name": "Team Beta", "description": "The second team"}
        ],
        "activities": [
            {"name": "Running", "calories_burned": 300},
            {"name": "Cycling", "calories_burned": 250}
        ],
        "leaderboard": [
            {"user": "john_doe", "score": 1500},
            {"user": "jane_doe", "score": 1200}
        ],
        "workouts": [
            {"name": "Morning Run", "duration": 30, "activity": "Running"},
            {"name": "Evening Cycle", "duration": 45, "activity": "Cycling"}
        ]
    }
