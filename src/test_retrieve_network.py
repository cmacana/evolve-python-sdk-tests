import asyncio
import argparse

from zepben.evolve import connect_async, NetworkConsumerClient
from zepben.evolve import Equipment


def print_feeder_eq(service):
    for equip in service.objects(Equipment):
        print(equip.mrid, equip.name, type(equip).__name__, equip.get_base_voltage())


async def main():
    parser = argparse.ArgumentParser(description="Integration Test of retrieve_network")
    parser.add_argument('server', help='Host and port of grpc server', metavar="host:port", nargs="?",
                        default="ewb.essentialenergy.zepben.com")
    parser.add_argument('--rpc-port', help="The gRPC port for the server", default="9014")
    args = parser.parse_args()
    async with connect_async(host=args.server, rpc_port=args.rpc_port) as channel:
        client = NetworkConsumerClient(channel)
        result = (await client.retrieve_network()).throw_on_error()
        service = result.result.network_service
        print_feeder_eq(service)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
