class ModelVaccumAgent:
    def __init__(self):
        self.room_status = {"A": "Dirty", "B": "Dirty"}
        
    def action(self, sense):
        place, position = sense
        
        self.room_status[place] = position
        
        if position == "Dirty":
            return "Suck"
        
        if self.room_status["A"] == "Clean" and self.room_status["B"] == "Clean":
            return "NoAction"
        
        return "Move"
    
modelVacuum = ModelVaccumAgent()

print(modelVacuum.action(("A", "Dirty")))
print(modelVacuum.action(("A", "Clean")))
print(modelVacuum.action(("B", "Dirty")))
print(modelVacuum.action(("B", "Clean")))