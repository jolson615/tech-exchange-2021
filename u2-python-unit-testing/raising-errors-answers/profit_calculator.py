from raise_error import check_nonnegative_number

def calculate_funding(backers, unit_cost):
    '''Returns the funding total (float) given a number of backers and cost per unit'''
    check_nonnegative_number(backers)
    check_nonnegative_number(unit_cost)
    total = backers * unit_cost
    return total

def calculate_campaign_costs(funding_total):
    '''Calculates the advertising costs, site fees, and fulfillment costs of a given funding total'''
    check_nonnegative_number(funding_total)
    advertising_costs = 500
    crowdfund_site_costs = funding_total*0.05
    fulfillment_costs = funding_total*0.05
    return crowdfund_site_costs + fulfillment_costs + advertising_costs

def calculate_personnel_costs(funding_total):
    '''Calculates the amount owed to each project contributer based on the funding total'''
    check_nonnegative_number(funding_total)
    phim = 500.0 + (funding_total*0.05)
    ahzam = 500.0 + (funding_total*0.05)
    ella = 2000.0
    return phim + ahzam + ella

def calculate_printing_costs(units):
    '''Returns the cost of printing a given number of board game units'''
    check_nonnegative_number(units)
    printer_fee = 1000.0 + (units * 10.0)
    shipping_fee = 250 + (units * 2)
    return printer_fee + shipping_fee

def calculate_profit(backers, unit_cost):
    funding = calculate_funding(backers, unit_cost)
    campaign_costs = calculate_campaign_costs(funding)
    personnel_costs = calculate_personnel_costs(funding)    
    print_costs = calculate_printing_costs(backers)
    net_profit = funding - (campaign_costs+personnel_costs+print_costs)
    return net_profit
