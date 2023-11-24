class csp:
    def __init__(self, variables, Domains,constraints): 
        self.variables = variables 
        self.domains = Domains 
        self.constraints = constraints 
        self.solution = None
        
    
    def solve(self):
        assignment = {}
        self.solutions = self.backtrack(assignment) 
        return self.solutions
    
    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment
        
        var = self.select_min_domain(assignment)
        
        for value in self.get_domains(var, assignment):
            if self.is_consistent(var, value, assignment): 
                assignment[var] = value 
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                
                del assignment[var] 
        return None

    
    def get_domains(self, var, assignment):
        return self.domains[var]
    
    def select_min_domain(self, assignment):
        unassigned_vars = [var for var in self.variables if var not in assignment]
        return min(unassigned_vars, key=lambda var : len(self.domains[var]))

    def is_consistent(self, var, value, assignment):
        for consistent in self.constraints[var]:
            if (consistent in assignment) and (assignment[consistent] == value):
                return False
            return True
        