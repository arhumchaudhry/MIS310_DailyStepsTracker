# function to set daily steps goal
def set_steps_goal():
    goal = int(input("Enter your daily steps goal: "))
    return goal


# function to record steps for 7 days
def record_daily_steps():
    total_steps = 0

    for day in range(1, 8):
        steps = int(input(f"Enter steps for day {day}: "))
        total_steps = total_steps + steps

    return total_steps


# function to evaluate performance
def evaluate_weekly_performance(total_steps, goal):
    average_steps = total_steps / 7

    print(f"\nAverage daily steps: {average_steps}")

    if average_steps > goal:
        print(f"You exceeded your daily steps goal!")
    elif average_steps == goal:
        print(f"You met your daily steps goal!")
    else:
        print(f"You did not meet your daily steps goal.")


# main function
def main():
    goal = set_steps_goal()
    total_steps = record_daily_steps()
    evaluate_weekly_performance(total_steps, goal)


# start program
main()
