import os
import subprocess
import sys

BASE_DIR = '/Users/Maulana/Documents/CODING/JURNAL/ML/project'

def run_pump_predictor():
    predictor_script = os.path.join(BASE_DIR, 'pump_predictor', 'main.py')
    env = os.environ.copy()
    env['PYTHONPATH'] = f"{BASE_DIR}:{env.get('PYTHONPATH', '')}"
    try:
        subprocess.run([sys.executable, predictor_script], check=True, env=env)
    except subprocess.CalledProcessError as e:
        print(f"Pump Predictor encountered an error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while running Pump Predictor: {e}")

def run_pump_inspector():
    inspector_script = os.path.join(BASE_DIR, 'pump_inspector.py')
    try:
        subprocess.run([sys.executable, inspector_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Pump Inspector encountered an error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while running Pump Inspector: {e}")

if __name__ == "__main__":
    print("Running Pump Predictor...")
    run_pump_predictor()
    
    print("\nRunning Pump Inspector...")
    run_pump_inspector()
    
    print("\nBoth programs have been executed.")
