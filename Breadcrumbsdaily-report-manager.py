import os
import time
import json
from datetime import datetime

# Constants
REPORTS_FOLDER = "data_collect"
OBJECTIVES_FILE = "objectives.json"
AUTH_FILE = "auth.json"
EXIT_KEY = "q"  # Define the key to exit the program

def get_filename():
    now = datetime.now()
    return now.strftime("%d%m%y_%H%M.log")

def load_objectives():
    if not os.path.exists(OBJECTIVES_FILE):
        return {}
    with open(OBJECTIVES_FILE, 'r') as f:
        return json.load(f)

def save_objectives(objectives):
    with open(OBJECTIVES_FILE, 'w') as f:
        json.dump(objectives, f, indent=4)

def authenticate_user():
    if not os.path.exists(AUTH_FILE):
        print("No authentication file found. Please set up authentication first.")
        return False

    with open(AUTH_FILE, 'r') as f:
        auth_data = json.load(f)
    
    username = input("Enter username: ")
    password = input("Enter password: ")

    if auth_data.get(username) == password:
        return True
    else:
        print("Authentication failed.")
        return False

def setup_authentication():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open(AUTH_FILE, 'w') as f:
        json.dump({username: password}, f, indent=4)
    
    print("Authentication setup completed.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def create_day_report():
    print("Creating Day Report...\n======================\n")
    achieved = input("What was achieved? ")
    progress = input("The progress? ")
    obstacles = input("Obstacles? ")
    tasks = input("Tomorrow's tasks and areas of focus on? ")
    alignment = input("Confirm you’re aligned with the original goals (y/n)? ")
    
    filename = get_filename()
    with open(os.path.join(REPORTS_FOLDER, filename), 'w') as f:
        f.write(f"What was achieved: {achieved}\n")
        f.write(f"The progress: {progress}\n")
        f.write(f"Obstacles: {obstacles}\n")
        f.write(f"Tomorrow's tasks and areas of focus on: {tasks}\n")
        f.write(f"Aligned with original goals: {alignment}\n")
    
    print(f"\n\nReport saved as {filename}")

def show_objective_and_purpose():
    objectives = load_objectives()
    print("Showing Objectives and Identifying Purpose...\n=============================================\n")
    
    # Filter numeric keys and sort
    numeric_objectives = {k: v for k, v in objectives.items() if k.isdigit()}
    sorted_objectives = sorted(numeric_objectives.items(), key=lambda x: int(x[0]))
    
    for serial, obj in sorted_objectives:
        print(f"Serial {serial}: {obj['Objective']}")
        print(f"Purpose: {obj['Purpose']}\n")

def update_objectives():
    objectives = load_objectives()
    print("Update Objectives and Purposes:")
    
    # Determine the next serial number
    serial_numbers = [int(k) for k in objectives if k.isdigit()]
    next_serial = max(serial_numbers, default=0) + 1
    serial = str(next_serial)
    
    objective = input("Create the Objective for the Next 5 Days: ")
    purpose = input("Identify Purpose: ")
    
    objectives[serial] = {"Objective": objective, "Purpose": purpose}
    save_objectives(objectives)
    print(f"New objective added with Serial {serial}.")

def review_past_reports():
    input("Day 6: Reviewing past 5 days' reports...\n----------------------------------------\n\n\nDay 6 main objective: Review progress and solve any lingering problems\n\nGuide to Analyze\nStep 1: Read each report carefully to understand the content\nStep 2: Categorize information into progress, challenges, and improvements\nPress any key to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    report_files = sorted([f for f in os.listdir(REPORTS_FOLDER) if f.endswith('.log')])
    
    if not report_files:
        print("No reports found.")
        return
    
    for file in report_files:
        with open(os.path.join(REPORTS_FOLDER, file), 'r') as f:
            print(f"\n--- {file} ---")
            print(f.read())
    
    accomplishments = input("Accomplishments: ")
    progress = input("Progress (in %): ")
    problems = input("Identify Problems: ")
    confusion = input("Areas that caused confusion or difficulty: ")
    clarifications = input("Clarifications for the problem: ")
    improvements = input("What needs improvement: ")
    
    filename = get_filename()
    with open(os.path.join(REPORTS_FOLDER, filename), 'w') as f:
        f.write(f"Accomplishments: {accomplishments}\n")
        f.write(f"Progress (in %): {progress}\n")
        f.write(f"Identify Problems: {problems}\n")
        f.write(f"Areas that caused confusion or difficulty: {confusion}\n")
        f.write(f"Clarifications for the problem: {clarifications}\n")
        f.write(f"What needs improvement: {improvements}\n")
    
    print(f"Review report saved as {filename}")

def edit_report():
    report_files = sorted([f for f in os.listdir(REPORTS_FOLDER) if f.endswith('.log')])
    
    if not report_files:
        print("No reports available to edit.")
        return
    
    print("Select a report to edit:")
    for i, file in enumerate(report_files, 1):
        print(f"{i}: {file}")
    
    choice = input("Enter the number of the report to edit: ")
    
    try:
        index = int(choice) - 1
        if 0 <= index < len(report_files):
            filename = report_files[index]
            with open(os.path.join(REPORTS_FOLDER, filename), 'r') as f:
                content = f.read()
            print(f"Current content of {filename}:\n{content}")
            new_content = input("Enter the new content (or type 'cancel' to abort): ")
            
            if new_content.lower() != 'cancel':
                with open(os.path.join(REPORTS_FOLDER, filename), 'w') as f:
                    f.write(new_content)
                print(f"Report {filename} has been updated.")
            else:
                print("Edit canceled.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def day_seven_actions():
    input("Day 7: Review the 6th Day’s Report and set the program\n------------------------------------------------------\nPress any key to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    input("Day 7 main objective: Read the 6th log file and set the new Objective and Identify Purpose for the next 5 days\nPress any key to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')    
    choice = input("[1] ADD\n[2] EDIT\n[3] DISPLAY\n[4] EXPORT\nChoose an option: ")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == "1":
        print("Adding new objectives...")
        objective = input("Create the Objective for the Next 5 Days: ")
        purpose = input("Identify Purpose: ")
        
        objectives = load_objectives()
        
        # Determine the next serial number
        serial_numbers = [int(k) for k in objectives if k.isdigit()]
        next_serial = max(serial_numbers, default=0) + 1
        serial = str(next_serial)
        objectives[serial] = {"Objective": objective, "Purpose": purpose}
        save_objectives(objectives)
        print(f"New objective added with Serial {serial}.")
    elif choice == "2":
        update_objectives()
    elif choice == "3":
        show_objective_and_purpose()
    elif choice == "4":
        print("Export functionality not implemented yet.")
    else:
        print("Invalid choice.")

def main():
    os.makedirs(REPORTS_FOLDER, exist_ok=True)
    
    while True:
        if not authenticate_user():
            print("Authentication required. Please set up or log in.")
            setup_authentication()
            continue
        
        day = input("\nSelect a day of the week (1 -7) or press 'q' to exit: \n")
        os.system('cls' if os.name == 'nt' else 'clear')        
        if day == EXIT_KEY:
            print("Exiting program...")
            break
        
        if day == "1":
            choice = input("Day 1: Starting\n---------------\n\n[1] Show Objective and Identify Purpose\n[2] Create Day Report\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice == "1":
                show_objective_and_purpose()
            elif choice == "2":
                create_day_report()
        
        elif day == "2":
            input("Day 2: Briefly revisit the purpose and goal\n-------------------------------------------\n\nPress any key to continue...")
            choice = input("\n[1] Show Objective and Identify Purpose\n[2] Create Day Report\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice == "1":
                show_objective_and_purpose()
            elif choice == "2":
                create_day_report()
        
        elif day == "3":
            input("Day 3: Reiterate the goals set for Day 2\n----------------------------------------\n\nPress any key to continue...")
            choice = input("\n[1] Show Objective and Identify Purpose\n[2] Create Day Report\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice == "1":
                show_objective_and_purpose()
            elif choice == "2":
                create_day_report()
        
        elif day == "4":
            input("Day 4: Stay on course with the day's plan\n-----------------------------------------\n\nPress any key to continue...")
            choice = input("\n[1] Show Objective and Identify Purpose\n[2] Create Day Report\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice == "1":
                show_objective_and_purpose()
            elif choice == "2":
                create_day_report()
        
        elif day == "5":
            input("Day 5: Continue with the program as planned\n-------------------------------------------\nPress any key to continue...")
            choice = input("[1] Show Objective and Identify Purpose\n[2] Create Day Report\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice == "1":
                show_objective_and_purpose()
            elif choice == "2":
                create_day_report()
        
        elif day == "6":
            review_past_reports()
        
        elif day == "7":
            day_seven_actions()
        
        elif day == "edit":
            edit_report()
        
        else:
            print("Invalid choice, please select a number between 1 and 7 or 'q' to exit.")
        
        input("Press any key to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
