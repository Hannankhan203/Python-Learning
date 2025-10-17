class ModelBasedVacuumAgent() :
    def __init__(self,init_a, init_b) :
        self.model = {"Loc_a" : init_a, "Loc_b" : init_b}
    def DoAction(self,location, status) :
        self.model[location] = status
        print(self.model)
        if self.model["Loc_a"] == self.model["Loc_b"] == 'clean' :
            return 'NoOp'
        elif status == 'dirty' :
            return 'suck'
        elif location == "Loc_a" :
            return 'right'
        else:
            return 'left'
a = ModelBasedVacuumAgent('clean', 'clean')
print(a.DoAction("Loc_a", 'clean'))