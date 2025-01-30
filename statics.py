from datetime import datetime, timezone

# List of allowed origins
ORIGINS = ["http://localhost:8000",
           "https://localhost:8000"
           ]

# Data to return
data = {
    "email": "sulaimonsalako20@gmail.com",
    "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "github_url": "<https://github.com/Sulai-maan/stage_0>"
}