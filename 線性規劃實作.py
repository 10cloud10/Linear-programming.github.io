
from scipy.optimize import linprog
'''
#測試
MIN
C = [-1,4] 
A = [[-3,1],[1,2]]
b = [6,4]
X0_bounds = [None,None]
X1_bounds = [-3,None]
res = linprog(C,A,b,bounds=(X0_bounds,X1_bounds))
print(res)

MAX
C = [1,-4] 
A = [[-3,1],[1,2]]
b = [6,4]
X0_bounds = [None,None]
X1_bounds = [-3,None]
res = linprog(C,A,b,bounds=(X0_bounds,X1_bounds))
print(res)
'''

#scipy.optimize.linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None, method='simplex', callback=None, options=None)
'''

Max 7T+5C
ST ->
3T+4C <= 2400
2T+1C <= 1000
C <= 450
T >= 100
T,C >= 0
'''
'''
C = [-7,-5] 
A = [[3,2],[4,1]]
b = [2400,1000]
X0_bounds = [100,None]
X1_bounds = [None,450]
res = linprog(C,A,b,bounds=(X0_bounds,X1_bounds))
print(res)
'''

import pulp as pulp

#建立問題
'''
# 求最小值
minimum_problem = pulp.LpProblem("problemName", pulp.LpMinimize)
 
# 求最大值
maximum_problem = pulp.LpProblem("problemName", pulp.LpMaximize)
'''

#建立變數
'''
# 建立 x 變數，範圍 (-∞, ∞)，值為 continuous
continous_x = pulp.LpVariable("x", lowBound=None, upBound=None, cat='Continuous')
 
# 建立 y 變數，範圍 [-10.5, 10.5]，值為 continuous
continous_y = pulp.LpVariable("y", lowBound=-10.5, upBound=10.5, cat='Continuous')
 
# 建立 z 變數，範圍 [0, ∞)，值為 Integer
interger_z = pulp.LpVariable("z", lowBound=0, upBound=None, cat='Integer')
 
# 建立 s 變數，範圍 [0, 1]，值為 Binary
binary_s = pulp.LpVariable("status", lowBound=0, upBound=None, cat='Binary')
 
# 建立多個變數，格式為 dicts
quantities = pulp.LpVariable.dicts("quantities", indexs=["shoes", "pen", "paper"])
# {'shoes': quantities_shoes, 'pen': quantities_pen, 'paper': quantities_paper}
 
# 可用 % format，但注意需包含 indexs 的部分
# 共需 len(indexStart) + 1 個 %
quantities = pulp.LpVariable.dicts("quantities_%s_%s", indexs=["shoes", "pen", "paper"], lowBound=None, upBound=None, cat="Continuous", indexStart=["for"])
# {'shoes': quantities_for_shoes,
#  'pen': quantities_for_pen,
#  'paper': quantities_for_paper}
'''

#建立數學方程式
'''
var = pulp.LpVariable.dicts("", ["x", "y", "z"])
var = {var["x"]:1, var["y"]:2, var["z"]:3}
# by 係數建立 1*x + 2*y + 3*z + 10，以下三者等效
formula_1 = pulp.LpAffineExpression(var, constant=10)
formula_2 = pulp.LpAffineExpression([(a,x) for a,x in var.items()], constant=10)
formula_3 = pulp.lpSum([a*x for a,x in var.items()]) + 10
'''

#建立不等式
'''
var = pulp.LpVariable.dicts("", ["x", "y", "z"])
# 直接寫，必須為 ==, >=, <=
equation_1 = var["x"] + var["y"] == 5
inequality_2 = var["x"] + var["z"] <= 10
inequality_2 = var["y"] + var["z"] >= -6
 
formula = pulp.LpAffineExpression([(var["x"],2), (var["y"],3), (var["z"],5)], constant=10)
# 可再用上面的方程式，轉為其他不等式
# 可以是直覺性寫法，需為 ==, >=, <= 或是 用 LpConstraint 建立
# 以下兩兩等效
formula >= 1
pulp.LpConstraint(formula, pulp.LpConstraintGE, rhs=1)
formula == 1
pulp.LpConstraint(formula, pulp.LpConstraintEQ, rhs=1)
formula <= 1
pulp.LpConstraint(formula, pulp.LpConstraintLE, rhs=1)
'''

#第一題
'''
Max 7T+5C
ST ->
3T+4C <= 2400
2T+1C <= 1000
C <= 450
T >= 100
T,C >= 0
'''
'''
#變數
T = pulp.LpVariable("T", lowBound=0, upBound=None, cat='Integer')
C = pulp.LpVariable("C", lowBound=0, upBound=None, cat='Integer')

#宣告問題
prob = pulp.LpProblem("problemName", pulp.LpMaximize)

#目標式
prob += 7*T + 5*C

#限制式
prob += 3*T+4*C <= 2400
prob += 2*T+C <= 1000
prob += C <= 450
prob += T >= 100

status = prob.solve()
print((status,pulp.LpStatus[status]))
print((pulp.value(T), pulp.value(C), pulp.value(prob.objective)))
'''

#第二題
'''
Min 0.10A + 0.15B
ST ->
5A+10B >= 45
4A+3B >= 24
0.5A >=1.5
'''
'''
#變數
A = pulp.LpVariable("A", lowBound=0, upBound=None, cat='simple')
B = pulp.LpVariable("B", lowBound=0, upBound=None, cat='simple')

#宣告問題
prob = pulp.LpProblem("problemName", pulp.LpMinimize)

#目標式
prob += 0.10*A + 0.15*B

#限制式
prob += 5*A+10*B >= 45
prob += 4*A+3*B >= 24
prob += 0.5*A >= 1.5

status = prob.solve()
print((status,pulp.LpStatus[status]))
print((pulp.value(A), pulp.value(B), pulp.value(prob.objective)))
'''

#第三題
'''
Max 200000I + 80000A
ST ->
3000I + 900A <= 75000
-5I + A <= 0
A , I >= 0
'''
'''
#變數
I = pulp.LpVariable("I", lowBound=0, upBound=None, cat='Integer')
A = pulp.LpVariable("A", lowBound=0, upBound=None, cat='Integer')

#宣告問題
prob = pulp.LpProblem("problemName", pulp.LpMaximize)

#目標式
prob += 200000*I + 80000*A

#限制式
prob += 3000*I + 900*A <= 75000
prob += -5*I + A <= 0

status = prob.solve()
print((status,pulp.LpStatus[status]))
print((pulp.value(I), pulp.value(A), pulp.value(prob.objective)))
'''

#第四題
'''
Min C30*0.12 + C92*0.09 + D21*0.11 + E11*0.04
ST ->
E11 >= 50*0.15
C92+C30 >= 50*0.45
D21+C92 <= 50*0.3
C30+C92+D21+E11 = 50
'''
'''
#變數
C30 = pulp.LpVariable("C30", lowBound=0, upBound=None, cat='simple')
C92 = pulp.LpVariable("C92", lowBound=0, upBound=None, cat='simple')
D21 = pulp.LpVariable("D21", lowBound=0, upBound=None, cat='simple')
E11 = pulp.LpVariable("E11", lowBound=0, upBound=None, cat='simple')

#宣告問題
prob = pulp.LpProblem("problemName", pulp.LpMinimize)

#目標式
prob += C30*0.12 + C92*0.09 + D21*0.11 + E11*0.04

#限制式
prob += E11 >= 50*0.15
prob += C92+C30 >= 50*0.45
prob += D21+C92 <= 50*0.3
prob += C30+C92+D21+E11 == 50

status = prob.solve()
print((status,pulp.LpStatus[status]))
print((pulp.value(C30), pulp.value(C92), pulp.value(D21), pulp.value(E11), pulp.value(prob.objective)))
'''