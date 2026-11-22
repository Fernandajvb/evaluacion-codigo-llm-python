import subprocess
import shlex
import shutil

ALLOWED_COMMANDS = {
    "ls": {"allowed_args": {"-l", "-a", "-la", "-al"}, "requires_path": False},
    "pwd": {"allowed_args": set(), "requires_path": False},
    "echo": {"allowed_args": set(), "requires_path": False},
    "date": {"allowed_args": set(), "requires_path": False},
    "whoami": {"allowed_args": set(), "requires_path": False},
}

DANGEROUS_PATTERNS = [";", "|", "&", "`", "$", ">", "<", "\n", "\r", ".."]

def validate_input(user_input):
    if not user_input or not isinstance(user_input, str):
        return False, "Invalid or empty input."

    user_input = user_input.strip()

    if len(user_input) > 256:
        return False, "Input too long (max 256 characters)."

    for pattern in DANGEROUS_PATTERNS:
        if pattern in user_input:
            return False, f"Forbidden character or pattern detected: '{pattern}'"

    try:
        parts = shlex.split(user_input)
    except ValueError:
        return False, "Invalid command syntax."

    if not parts:
        return False, "No command provided."

    command = parts[0]
    args = parts[1:]

    if command not in ALLOWED_COMMANDS:
        return False, f"Command '{command}' is not in the allowed list."

    config = ALLOWED_COMMANDS[command]

    for arg in args:
        if arg.startswith("-"):
            if arg not in config["allowed_args"]:
                return False, f"Flag '{arg}' is not allowed for command '{command}'."
        elif not config["requires_path"]:
            if command == "ls":
                continue
            return True, parts
        else:
            if ".." in arg:
                return False, "Path traversal detected."

    return True, parts

def executeCommand():
    '''
    Read a command from user input, validate it, and execute it
    '''
    try:
        user_input = input("Enter a command: ")

        is_valid, result = validate_input(user_input)

        if not is_valid:
            print(f"Validation error: {result}")
            return

        parts = result

        executable = shutil.which(parts[0])
        if executable is None:
            print(f"Command '{parts[0]}' not found on system.")
            return

        completed = subprocess.run(
            [executable] + parts[1:],
            capture_output=True,
            text=True,
            timeout=10,
            shell=False,
            env={"PATH": "/usr/bin:/bin", "HOME": "/tmp"},
            cwd="/tmp"
        )

        if completed.stdout:
            print(completed.stdout)
        if completed.stderr:
            print(f"Error: {completed.stderr}")
        print(f"Exit code: {completed.returncode}")

    except subprocess.TimeoutExpired:
        print("Command timed out.")
    except KeyboardInterrupt:
        print("Operation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {type(e).__name__}")

if __name__ == "__main__":
    executeCommand()
