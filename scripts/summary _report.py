# Function to read the log file
import os

def read_log_file(file_path):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path for the results folder
    results_folder = os.path.join(script_dir, '..', 'results')

    # Ensure the results folder exists
    os.makedirs(results_folder, exist_ok=True)
    
    # Construct the full path to the log file
    file_path = os.path.join(results_folder, file_path)

    # Read the log file
    with open(file_path, 'r') as file:
        logs = file.readlines()

    # Filter out the suspicious logs
    # Classify the logs into FAILED and ERROR
    suspicious_logs = {
        'FAILED': [],
        'ERROR': []
    }
    for log in logs:
        if 'failed' in log.lower():
            suspicious_logs['FAILED'].append(log.lower())
        elif 'error' in log.lower():
            suspicious_logs['ERROR'].append(log.lower())

    # Construct the path for the results folder
    results_folder = os.path.join(script_dir, '..', 'Results')

    # Ensure the results folder exists
    os.makedirs(results_folder, exist_ok=True)
    
    # Construct the path for the summary report
    summary_report_path = os.path.join(results_folder, 'summary_report.txt')

    # Generate the summary report
    # Logs the amount of each type of log and the logs for each type
    with open(summary_report_path, 'w') as f:
        for type, logs in suspicious_logs.items():
            f.write(f"Total {type.upper()} logs found: {len(logs)}\n\n")
            for log in logs:
                f.write(f"{type.upper()} log: {log}\n")
            f.write("\n")

    # Print that the summary report has been generated
    print("Summary report generated successfully!")

# The actual log file 
log_file_path = 'auth.log'
read_log_file(log_file_path)
