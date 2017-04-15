def calculate_tax(income_input):
    
    # define maximum tax rate and when it applies (income/max rate)
    maxinc = 50000; maxtax = 30
    
    # define tax ranges; bottom, top and the according tax percentage
    ranges = [   
        [0, 1000, 0],
        [1000, 10000, 10],
        [10000, 20200, 15],
        [20200, 30750, 20],
        [30750, 50000, 25],
        ]
    for key in income_input.items():
        
        #A dict to hold output
        taxes = dict()

        pay = []
        income = income_input[key]
        
        for r in ranges:
            if all([income_input[key] > r[0], income_input[key] > r[1]]):
                pay.append((r[1]-r[0]) * r[2]/100)
            elif all([income_input[key] > r[0], income_input[key] <= r[1]]):
                pay.append((income_input[key]-r[0]) * r[2]/100)
        
        if income_input[key] > maxinc:
            pay.append((income_input[key]-maxinc) * maxtax/100)

        else:
            pass

        taxes[key] = int(sum(pay))
    return income_input