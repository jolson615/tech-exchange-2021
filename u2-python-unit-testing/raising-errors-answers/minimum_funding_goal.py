from profit_calculator import calculate_profit
from profit_calculator import calculate_funding

def calculate_funding_goal(unit_cost, profit_goal):
    net_profit = -1.0
    backer_count = 0
    
    while net_profit < profit_goal:
        backer_count += 1
        net_profit = calculate_profit(backer_count, unit_cost)
    
    print("Minimun backer count:", backer_count)
    print("Minimum Funding Goal: ", calculate_funding(backer_count, unit_cost))
    print("Net Profit: ", net_profit)

calculate_funding_goal(30,2000)