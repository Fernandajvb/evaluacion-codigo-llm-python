import subprocess
import shlex
import sys

ALLOWED_COMMANDS = {"ls", "pwd", "whoami", "date", "echo"}

def executeCommand():
    try:
        command = input("Enter command: ").strip()
    except EOFError:
        return
    if not command:
        print("Error: empty command", file=sys.stderr)
        return
    try:
        args = shlex.split(command)
    except ValueError as e:
        print(f"Error: invalid command syntax: {e}", file=sys.stderr)
        return
    if not args:
        print("Error: empty command", file=sys.stderr)
        return
    cmd = args[0]
    if cmd not in ALLOWED_COMMANDS:
        print(f"Error: command '{cmd}' is not allowed", file=sys.stderr)
        return
    if any('\x00' in arg for arg in args):
        print("Error: invalid argument", file=sys.stderr)
        return
    try:
        result = subprocess.run(
            args,
            shell=False,
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
            stdin=subprocess.DEVNULL
        )
    except subprocess.TimeoutExpired:
        print("Error: command timed out", file=sys.stderr)
        return
    except FileNotFoundError:
        print(f"Error: command '{cmd}' not found", file=sys.stderr)
        return
    except Exception as e:
        print(f"Error: failed to execute command: {e}", file=sys.stderr)
        return
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    return result.returncode
