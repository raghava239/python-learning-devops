number_of_instances = 15
hourly_rate_usd = 0.0475
hours_in_month = 730

total_cost = number_of_instances * hourly_rate_usd * hours_in_month

print(f"The total cost of running {number_of_instances} instances for {hours_in_month} hours is ${total_cost:.2f}")