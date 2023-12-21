import datetime

super_saver_rate = 0.05
saver_rate = 0.11
peak_rate = 0.38

def calculate_cost(rate, duration):  
    return rate * duration

def calculate_usage(rate, duration):  
    usage = (rate / 60) * duration
    return usage

def get_applicable_rate(time_str):
    hour = int(time_str.split(":")[0])
    if 0 <= hour < 6:
        return super_saver_rate
    elif 6 <= hour < 16:
        return saver_rate
    elif 16 <= hour < 20:
        return peak_rate
    else:
        return saver_rate

def process_usage_records(usage_record):
    total_usage = 0
    total_cost = 0

    for record in usage_record:
        appliance, rate, start_time, duration = record
        applicable_rate = get_applicable_rate(start_time)

        usage = calculate_usage(rate, duration)
        cost = calculate_cost(applicable_rate, usage)

        print("{}: {:.2f}kWh, ${:.4f}".format(appliance, usage, cost))

        total_usage += usage
        total_cost += cost
    return total_usage, total_cost

usage_record = [
    ["dryer", 3, "08:00", 15],  
    ["dishwasher", 1.2, "19:30", 60],
    ["dishwasher", 1.2, "22:00", 30],
]

print("Electricity Usage and Cost Report:")

total_usage, total_cost = process_usage_records(usage_record)
print("Total electricity usage for the day: {:.2f} kWh".format(total_usage))
print("Total Cost for the Day: ${:.4f}".format(total_cost))
