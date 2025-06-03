import argparse

parser = argparse.ArgumentParser(
    prog="Tibian Bazaar Investigator",
)

command = parser.add_subparsers(title="commands", dest="command")

client_parser = command.add_parser(name="client", help="run TBI utility client")
client_parser.add_argument(
    "-g", "--get", metavar="CHARNAME", help="get data of CHARNAME", dest="charname"
)

server_parser = command.add_parser(name="server", help="Run TBI server")
server_parser.add_argument(
    "-a", "--address", default="0.0.0.0", help="server bind address"
)
server_parser.add_argument(
    "-p", "--port", default="8000", type=int, help="server bind port"
)
