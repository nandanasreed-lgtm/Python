days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
habit_tracker = (1, 0, 1, 1, 0, 1, 0)
habit_count = 0
for i in range(0,7):
    if habit_tracker[i] == 1:
        habit_count += 1
        print(f"On {days[i]}, you completed your habit!")
        print(f"Total habits completed so far: {habit_count}")
    if habit_count >= 5:
        print("Congratulations! You have completed your habit for 5 days this week!")
        break
    else:
        print(f"On {days[i]}, you did not complete your habit.")