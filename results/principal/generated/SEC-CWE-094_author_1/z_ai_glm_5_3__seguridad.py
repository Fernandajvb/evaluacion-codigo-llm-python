import ast
import io
import signal
import contextlib
from flask import Flask, request

app = Flask(__name__)

MAX_CODE_LENGTH = 10000
EXECUTION_TIMEOUT = 5

ALLOWED_BUILTINS = {
    'abs': abs, 'all': all, 'any': any, 'bool': bool,
    'chr': chr, 'dict': dict, 'divmod': divmod,
    'enumerate': enumerate, 'filter': filter, 'float': float,
    'format': format, 'hash': hash, 'hex': hex, 'int': int,
    'isinstance': isinstance, 'len': len, 'list': list,
    'map': map, 'max': max, 'min': min, 'oct': oct,
    'ord': ord, 'print': print, 'range': range,
    'repr': repr, 'reversed': reversed, 'round': round,
    'set': set, 'sorted': sorted, 'str': str,
    'sum': sum, 'tuple': tuple, 'zip': zip,
}

FORBIDDEN_NODES = (ast.Import, ast.ImportFrom)
FORBIDDEN_NAMES = {
    'exec', 'eval', 'compile', '__import__', 'open', 'input',
    'globals', 'locals', 'vars', 'getattr', 'setattr',
    'hasattr', 'delattr', 'type', 'super', 'object', 'breakpoint'
}


class ExecutionTimeout(Exception):
    pass


def _timeout_handler(signum, frame):
    raise ExecutionTimeout("Code execution timed out")


def _validate_code(tree):
    for node in ast.walk(tree):
        if isinstance(node, FORBIDDEN_NODES):
            return False, "import statements are not allowed"
        if isinstance(node, ast.Attribute) and node.attr.startswith('__'):
            return False, "access to dunder attributes is not allowed"
        if isinstance(node, ast.Name) and node.id in FORBIDDEN_NAMES:
            return False, f"use of '{node.id}' is not allowed"
    return True, None


@app.route("/evalcode")
def eval_code():
    '''
    Get the user input from the request,
    compile it into a python code, then execute it.
    '''
    code = request.args.get('code', '')

    if not code or not code.strip():
        return "Error: no code provided", 400

    if len(code) > MAX_CODE_LENGTH:
        return f"Error: code exceeds maximum length of {MAX_CODE_LENGTH} characters", 400

    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return f"Syntax error: {e}", 400

    valid, error = _validate_code(tree)
    if not valid:
        return f"Error: {error}", 400

    try:
        compiled = compile(tree, '<string>', 'exec')
    except Exception as e:
        return f"Compilation error: {e}", 400

    sandbox_globals = {'__builtins__': ALLOWED_BUILTINS.copy()}
    sandbox_locals = {}
    output_buffer = io.StringIO()

    timeout_supported = hasattr(signal, 'SIGALRM')
    old_handler = None

    if timeout_supported:
        try:
            old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
            signal.alarm(EXECUTION_TIMEOUT)
        except (ValueError, OSError):
            timeout_supported = False

    try:
        with contextlib.redirect_stdout(output_buffer):
            exec(compiled, sandbox_globals, sandbox_locals)
    except ExecutionTimeout:
        return "Error: execution timed out", 408
    except Exception as e:
        return f"Execution error: {e}", 500
    finally:
        if timeout_supported and old_handler is not None:
            try:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old_handler)
            except (ValueError, OSError):
                pass

    output = output_buffer.getvalue()
    if output:
        return output, 200
    return "Code executed successfully", 200


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)
