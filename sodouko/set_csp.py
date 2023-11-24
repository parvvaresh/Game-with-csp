class set_csp:
    def __init__(self):
        pass

    
    def _varables(self):
        varables =  [
            (i , j) for i in range(9) for j in range(9)
        ]
        return varables
    
    def _domains(self, puzzel, varables):
        doamins = dict()
        for var in varables:
            if puzzel[var[0]][var[1]] == 0:
                doamins[var] = list(range(1, 10))
            else:doamins[var] = [puzzel[var[0]][var[1]]]
        return doamins

    def _set_constraints(self, var):
        constraints = []
        for index in range(9):
            if index != var[0]:
                constraints.append((index , var[1]))
            if index != var[1]:
                constraints.append((var[0], index))
            
        sub_i , sub_j = var[0] // 3, var[1] // 3
        for i in range(sub_i * 3 , (sub_i + 1) * 3):
            for j in range(sub_j * 3 , (sub_j + 1) * 3):
                if (i, j) != var:
                    constraints.append((i ,j))
                    
        return constraints

    def _constraints(self, varables):
        constraints = {}
        for var in varables:
            constraints[var] = self._set_constraints(var)
        return constraints
            
        
                    

                        
                        

                
                
                
            