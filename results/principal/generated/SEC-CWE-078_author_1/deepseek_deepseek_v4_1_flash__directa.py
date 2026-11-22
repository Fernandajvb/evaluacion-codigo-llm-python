import subprocess
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    command = input("Enter command: ").strip()
    if not command:
        print("No command provided.")
        return
    forbidden = set(';|&$><`\\')
    if any(c in forbidden for c in command):
        print("Invalid command: contains forbidden characters.")
        return
    try:
        args = shlex.split(command)
    except ValueError as e:
        print(f"Invalid command: {e}")
        return
    if not args:
        print("No command provided.")
        return
    try:
        result = subprocess.run(args, shell=False, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e.stderr}")
    except FileNotFoundError:
        print("Command not found.")
