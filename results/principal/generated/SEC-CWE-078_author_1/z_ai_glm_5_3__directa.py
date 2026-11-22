import subprocess
import shlex

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    # Whitelist of allowed commands (validation against command injection)
    allowed_commands = {'ls', 'pwd', 'date', 'whoami', 'echo'}

    # Read command from user input
    try:
        command = input("Enter a command: ").strip()
    except EOFError:
        return

    if not command:
        print("Error: no command entered.")
        return

    # Parse safely without invoking a shell
    try:
        parts = shlex.split(command)
    except ValueError as e:
        print(f"Error: invalid command syntax: {e}")
        return

    if not parts:
        print("Error: no command entered.")
        return

    # Validate the command name against the whitelist
    if parts[0] not in allowed_commands:
        print(f"Error: command '{parts[0]}' is not allowed.")
        return

    # Execute the validated command safely (no shell=True)
    try:
        result = subprocess.run(
            parts,
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.stdout:
            print(result.stdout, end='')
        if result.stderr:
            print(result.stderr, end='')
        print(f"Return code: {result.returncode}")
    except subprocess.TimeoutExpired:
        print("Error: command execution timed out.")
    except FileNotFoundError:
        print(f"Error: executable '{parts[0]}' not found.")
    except Exception as e:
        print(f"Error executing command: {e}")


if __name__ == "__main__":
    executeCommand()
