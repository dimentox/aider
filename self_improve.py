import os
import subprocess

def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))

def get_version():
    try:
        result = subprocess.run(['pip', 'show', 'aider'], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if line.startswith('Version:'):
                return line.split(' ')[1]
    except Exception as e:
        return str(e)

def self_improve():
    # Placeholder for self-improvement logic
    print("Self-improvement logic goes here")

if __name__ == "__main__":
    print("Current Directory:", get_current_directory())
    print("Version:", get_version())
    self_improve()
