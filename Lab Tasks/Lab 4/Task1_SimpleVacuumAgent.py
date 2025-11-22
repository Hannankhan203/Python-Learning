class VacuumAgent:
    def action(self, sense):
        place, position = sense
        
        if position == "Dirty":
            return "Suck"
        elif position == "Clean":
            return "Move"
        
simpleVacuum = VacuumAgent()

print(simpleVacuum.action(("A", "Clean")))
print(simpleVacuum.action(("B", "Dirty")))
print(simpleVacuum.action(("C", "Dirty")))
print(simpleVacuum.action(("D", "Clean")))