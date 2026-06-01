class Step:
    def __init__(self, description: str, timer: int = 0):
        self.description = description
        self.timer = timer

    def to_dict(self):
        return {
            "description": self.description,
            "timer": self.timer
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["description"],
            data.get("timer", 0)
        )

    def __str__(self):
        if self.timer:
            return f"{self.description} ({self.timer} min)"
        return self.description