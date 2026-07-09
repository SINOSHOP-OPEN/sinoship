\"\"\"船舶模型模块\"\"\"

class Ship:
    \"\"\"船舶类\"\"\"
    def __init__(self, name: str, length: float):
        self.name = name
        self.length = length

    def info(self) -> str:
        return f\"Ship: {self.name}, Length: {self.length}m\"
