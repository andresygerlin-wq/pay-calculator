# Pay calculator

# Prompt the user for hours worked and rate
hours = input("Enter hours:")
rate = input("Enter rate:")
# Input error handling
try:
    float_hours = float(hours)
    float_rate = float(rate)
except:
    print("Error, please enter a numeric input")
# Calculate pay with overtime cinsideration
else:
    if float_hours > 40:
        base_pay = 40 * float_rate # Regular hours pay calculation
        overtime_hours = (float_hours - 40) # Extra hours
        overtime_pay = overtime_hours * (float_rate * 1.5) # Extra pay
        extra_pay = base_pay + overtime_pay # Total pay
    else:
        extra_pay = float_hours * float_rate # When there are no extra hours
# Display total weekly pay
    print("Pay", extra_pay)