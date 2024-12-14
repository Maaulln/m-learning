import csv
from datetime import datetime
import os

# Define the base directory
BASE_DIR = '/Users/Maulana/Documents/CODING/JURNAL/ML/project'

def check_pump_condition(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        logs = []
        
        for row in reader:
            malfunction_indicator = int(row['malfunction_indicator'])
            if malfunction_indicator > 0:
                message = f"Warning: Pump malfunction detected at {row['runtime_hours']} hours."
                if malfunction_indicator == 1:
                    message += " Minor issue, needs attention."
                elif malfunction_indicator == 2:
                    message += " Moderate issue, requires prompt inspection."
                elif malfunction_indicator == 3:
                    message += " Serious issue, immediate repair needed!"
                logs.append(message)
        
        return logs

def generate_log(logs):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_name = f"pump_inspection_log_{timestamp}.txt"
    log_file_path = os.path.join(BASE_DIR, 'logs', log_file_name)
    
    # Ensure the logs directory exists
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    
    with open(log_file_path, 'w') as logfile:
        logfile.write(f"Pump Inspection Log - {timestamp}\n")
        logfile.write("=====================================\n\n")
        for log in logs:
            logfile.write(log + "\n")
        logfile.write("\nEnd of inspection log.")
    
    return log_file_path

# Main execution
csv_file_path = os.path.join(BASE_DIR, 'data', 'pump_data.csv')
inspection_logs = check_pump_condition(csv_file_path)
log_file = generate_log(inspection_logs)

print(f"Inspection complete. Log file generated: {log_file}")
print("\nLog contents:")
with open(log_file, 'r') as f:
    print(f.read())
