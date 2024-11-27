from xmlrpc.client import ServerProxy
import sys

if __name__ == "__main__":
    # Ensure proper arguments
    if len(sys.argv) != 5:
        print("Usage: python client.py <host> <port> <x> <y>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    x = float(sys.argv[3])
    y = float(sys.argv[4])

    # Connect to the server
    server_url = f"http://{host}:{port}/"
    proxy = ServerProxy(server_url)

    # Perform operations
    print(f"Server name: {proxy.name()}")
    print(f"Help: {proxy.help()}")
    print(f"Server time: {proxy.servertime()}")
    print(f"{x} + {y} is {proxy.add(x, y)}")
    print(f"{x} - {y} is {proxy.sub(x, y)}")
    print(f"{x} * {y} is {proxy.mult(x, y)}")
    print(f"{x} / {y} is {proxy.div(x, y)}")
    print(f"{x} / 0 is {proxy.div(x, 0)}")  # Test divide by zero
