class Process:
    def __init__(self, p_id, name, start_time, priority):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"{self.p_id}\t{self.name}\t{self.start_time}\t{self.priority}"

def sort_processes(processes, sort_key):
    if sort_key == 1:
        return sorted(processes, key=lambda p: int(p.p_id[1:]))
    elif sort_key == 2:
        return sorted(processes, key=lambda p: p.start_time)
    elif sort_key == 3:
        priority_order = {"Low": 0, "MID": 1, "High": 2}
        return sorted(processes, key=lambda p: priority_order[p.priority])

def main():
    processes = [
        Process("P1", "VSCode", 100, "MID"),
        Process("P23", "Eclipse", 234, "MID"),
        Process("P93", "Chrome", 189, "High"),
        Process("P42", "JDK", 9, "High"),
        Process("P9", "CMD", 7, "High"),
        Process("P87", "NotePad", 23, "Low")
    ]

    while True:
        print("\nMenu:")
        print("1. Sort by Process ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                sorted_processes = sort_processes(processes, choice)
                print_sorted_processes(sorted_processes)
            elif choice == 2:
                sorted_processes = sort_processes(processes, choice)
                print_sorted_processes(sorted_processes)
            elif choice == 3:
                sorted_processes = sort_processes(processes, choice)
                print_sorted_processes(sorted_processes)
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid choice.")

def print_sorted_processes(sorted_processes):
    print("\nSorted Processes:")
    print("ID\tName\tStart Time\tPriority")
    print("-" * 35)
    for process in sorted_processes:
        print(process)

if __name__ == "__main__":
    main()

