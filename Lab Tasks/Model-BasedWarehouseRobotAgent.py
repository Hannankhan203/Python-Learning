class ModelWarehouseAgent:
    def __init__(self):
        self.picked_items = {}
        
    def action(self, sense):
        place, hasPackage = sense
        
        if hasPackage == "Yes":
            if place not in self.picked_items:
                self.picked_items[place] = True
                return "Pick"
            else:
                return "Skip"
        else:
            return "Move"
        
warehouse = ModelWarehouseAgent()
print(warehouse.action(("Shelf1", "Yes")))
print(warehouse.action(("Shelf1", "Yes")))
print(warehouse.action(("Shelf2", "No")))
print(warehouse.action(("Shelf2", "Yes")))
print(warehouse.action(("Shelf2", "Yes")))