from tbi.core.args import parser


def main():
    args = parser.parse_args()
    if args.command == "client":
        from tbi.core import client

        client.run(args)
    elif args.command == "server":
        from tbi.core import server

        server.run(args)
    else:
        parser.print_usage()
