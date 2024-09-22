# daily_reminder.py

# Prompt user for task details
task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = f"Task: {task} with {priority} priority"

# Match Case for task priority
match priority:
    case "high":
        reminder += " requires urgent attention."
    case "medium":
        reminder += " should be done soon."
    case "low":
        reminder += " can be handled later."
    case _:
        reminder += " has no recognized priority."

# Check if the task is time-sensitive
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the customized reminder
print(reminder)