class Step:
    def __init__(self, description: str, timer: int = 0):
        self.description = description
        self.timer = timer

    def __str__(self):
        if self.timer > 0:
            return f"{self.description} ({self.timer} min)"
        return self.description