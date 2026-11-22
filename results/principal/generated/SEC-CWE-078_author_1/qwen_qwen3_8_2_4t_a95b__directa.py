import subprocess
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    allowed_commands = {"ls", "pwd", "echo", "date", "whoami", "hostname"}

    user_input = input("Enter command: ")

    try:
        command_parts = shlex.split(user_input)
    except ValueError as exc:
        print(f"Invalid command: {exc}")
        return None

    if not command_parts:
        print("No command provided.")
        return None

    executable = command_parts[0]

    if "/" in executable or "\\" in executable:
        print("Command paths are not allowed.")
        return None

    if executable not in allowed_commands:
        print(f"Command not allowed: {executable}")
        return None

    forbidden_characters = set(";&|`$<>{}()\n\r")

    for argument in command_parts[1:]:
        if any(character in argument for character in forbidden_characters):
            print("Invalid characters in command arguments.")
            return None

    try:
        result = subprocess.run(
            command_parts,
            capture_output=True,
            text=True,
            timeout=10,
            check=False
        )

        if result.stdout:
            print(result.stdout, end="")

        if result.stderr:
            print(result.stderr, end="")

        return result.returncode

    except subprocess.TimeoutExpired:
        print("Command timed out.")
        return None

    except FileNotFoundError:
        print("Command not found.")
        return None

    except OSError as exc:
        print(f"Error executing command: {exc}")
        return None
