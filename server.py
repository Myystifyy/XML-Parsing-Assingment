from xmlrpc.server import SimpleXMLRPCServer
import sys
from datetime import datetime

def get_name():
    """Returns the server name passed during invocation."""
    return server_name

def get_help():
    """Returns a list of supported procedures."""
    return ["name", "help", "servertime", "add(x, y)", "sub(x, y)", "mult(x, y)", "div(x, y)"]

def get_servertime():
    """Returns the current server time in 24-hour format."""
    return datetime.now().strftime("%H:%M:%S")

def add(x, y):
    """Returns the sum of x and y."""
    return x + y

def sub(x, y):
    """Returns the difference (x - y)."""
    return x - y

def mult(x, y):
    """Returns the product of x and y."""
    return x * y

def div(x, y):
    """Returns the division (x / y), handles division by zero."""
    if y == 0:
        return "Infinity"
    return x / y

if __name__ == "__main__":
    # Ensure proper arguments
    if len(sys.argv) != 3:
        print("Usage: python server.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    server_name = "My XML-RPC Server"

    # Start the server
    with SimpleXMLRPCServer((host, port)) as server:
        print(f"Server listening on {host}:{port}")
        
        # Register functions
        server.register_function(get_name, "name")
        server.register_function(get_help, "help")
        server.register_function(get_servertime, "servertime")
        server.register_function(add, "add")
        server.register_function(sub, "sub")
        server.register_function(mult, "mult")
        server.register_function(div, "div")

        # Keep the server running
        server.serve_forever()
