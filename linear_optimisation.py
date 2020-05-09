# from pulp import LpProblem, LpVariable
import pulp as p


def readFile():
    t = []
    with open("input.txt", 'r') as file:
        n = 0
        for row in file:
            t.append(row.split(','))
            t[n] = [float(e) for e in t[n]]
            n += 1
    return t


def solveProblem(c):
    problem = p.LpProblem("Maximisation problem", p.LpMaximize)
    x1 = p.LpVariable("x1", 0, None, p.LpInteger)
    x2 = p.LpVariable("x2", 0, None, p.LpInteger)
    # objective function
    problem += c[0][0]*x1 + c[0][1]*x2, "Maximise" 
    for i in range(1, len(c)):
        # constraints are entered
        problem += c[i][0]*x1 + c[i][1]*x2 <= c[i][2], "Contstraint {}".format(i)
    problem.solve()
    return problem


def writeFile(c, problem):
    output = []
    with open("output.txt", "w") as file:
        file.write("Status:" + p.LpStatus[problem.status] + "\n")
        xlist = []
        for v in problem.variables():
            output.append(v.varValue)
            file.write(v.name + "=" + str(v.varValue) + "\n")
            xlist.append(v.varValue)
        file.write("Optimal Solution= {}".format(str(c[0][0]*xlist[0] + c[0][1]*xlist[1])))
    return output


x = readFile()
y = solveProblem(x)
z = writeFile(x, y)
print(y)
print("Solution found. Please refer to output.txt")
