import os
import psutil #Requires installing pstuil module

def log_performance():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path for the results folder
    results_folder = os.path.join(script_dir, '..', 'Results')

    # Ensure the results folder exists
    os.makedirs(results_folder, exist_ok=True)

    # Construct the path for the performance log
    performance_log_path = os.path.join(results_folder, 'performance_log.txt')

    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    # Get Memory usage
    memory_info = psutil.virtual_memory()
    print(f"Memory Usage: {memory_info.percent}%\n")

    # Log the data to performance_log.txt file
    with open(performance_log_path, 'a') as f:
        f.write(f"CPU: {cpu_usage}%, Memory: {memory_info.percent}%\n")

    # Print that the log was generated successfully
    print("Performance log generated successfully!")

    # Check if CPU usage is above 90%
    # If yes, print an alert
    if cpu_usage > 90:
        print("\nALERT: High CPU usage detected!")
        
log_performance()