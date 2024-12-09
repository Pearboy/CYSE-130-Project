## Project Overview: 
This cybersecurity system has been designed to monitor and enhance the security of a computer system through automated performance tracking, vulnerability scanning, and log analysis. The system aims to provide real-time alerts when CPU usage becomes excessive, generate detailed performance logs, scan networks for potential vulnerabilities, and analyze logs for suspicious activities. By utilizing Python scripts and tools such as nmap, this system ensures that potential security threats are identified and addressed promptly.

## Key Features: 
- Performance Log: Tracks CPU and memory usage, generates logs, and provides alerts for high CPU usage.
- Scan: Scans a target system using nmap to identify open ports and running services.
- Summary Report: Analyzes logs to identify and classify suspicious entries, such as errors or failed events.
- Alert Email: Sends an email notification when CPU usage exceeds a defined threshold.

## Installation: 
### Prerequisites:
- Python 3.x: Ensure python is install on the system
- Nmap: This tool is used for network scanning and must be installed

### Steps to Install:
1. Clone the repository:
    git clone [https://github.com/Pearboy/CYSE-Monitoring-System.git](https://github.com/Pearboy/CYSE-Monitoring-System.git)
2. Navigate to the projecet directory
    cd CYSE-Monitoring-System
3. Install neccessary Python liberies: Run the following command to install all the required depedencies from requirements.txt
    pip install -r scripts/requirements.txt
4. Install Nmap
- For Linux
    sudo apt install namp
- For MacOS
    brew install nmap
- For Windows
    Download and install from the [offical Nmap website](https://nmap.org/download.html#windows)

## Usage

- Tracks CPU and memory usage and generates a performance log file. Alerts are printed for high CPU usage.
    Run: python "scripts/performance_log.py"
- Performs a network scan on a target using nmap and captures packets to monitor source and destination IPs.
    Run: python "scripts/scan.py"
- Analyzes log files for errors or failed events and generates a summary report.
    Run: python "scripts/summary_report.py"
- Sends an email notification if CPU usage exceeds a specified threshold.
    Run: python "scripts/alert_email.py"

## Team Members 
- Ethan Le: Python Developer/Data Analyst
- Francis Abreu: Project Manager
- Sai: Data Analyst
- Abdulmohsen Almodiers: System Modelers
- Aneesh Ganesh: Python Developer
