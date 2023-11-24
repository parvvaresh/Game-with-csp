from board_game import board_game
from set_csp import set_csp
from csp import csp

game = board_game()



print("see this puzzel and we are solve it by csp ALG")
game.show_puzzel()


csp_det = set_csp()


variables = csp_det._varables()
Domains = csp_det._domains(game.get_puzzel() ,variables)
constraints = csp_det._constraints(variables)




solve = csp(variables, Domains,constraints)

ass = solve.solve()
puzzel = game.get_puzzel()

for var , sol in ass.items():
    
    puzzel[var[0]][var[1]] = sol

game.set_puzzel(puzzel)
print("this is a solve it!!!!!!!!!")
game.show_puzzel()

print(len(variables))

