class TrafficAgent:
    def action(self, color):
        traffic, light = color
        
        if light == "Red":
            return "Stop"
        elif light == "Yellow":
            return "Slow"
        elif light == "Green":
            return "Go"
        
trafficLight = TrafficAgent()

print(trafficLight.action(("A", "Green")))
print(trafficLight.action(("B", "Yellow")))
print(trafficLight.action(("C", "Red")))