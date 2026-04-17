# 1. Asking for information
balance = float(input("Starting balance: "))
monthly_deposit = float(input("Monthly savings amount: "))
months = int(input("How many months to simulate? "))
goal = 10000  # Let's set a savings goal

# 2.This runs once for every month
for month in range(1, months + 1):
    balance = balance + monthly_deposit
    
    # 3.Checking the progress
    if balance >= goal:
        print(f"Month {month}: ${balance} - GOAL REACHED! 🚀")
    else:
        print(f"Month {month}: ${balance}")

# 4. Final Summary
print("Simulation complete.")
