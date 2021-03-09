import argparse
import asyncio

from zepben.evolve import NetworkService, Equipment, Meter, UsagePoint
from zepben.evolve import connect_async, NetworkConsumerClient


def get_list_of_equipment(service):
    for eq in service.objects(Equipment):
        print(eq.mrid, eq.name, type(eq).__name__, eq.get_base_voltage())


def get_premise_id_by_equipment_mrid(service):
    for eq in service.objects(Equipment):
        for up in list(eq.usage_points):
            for mt in list(up.end_devices):
                print(f"The equipment {eq.name} has the premise ID {mt.service_location.name}")


def get_premise_ids(service):
    for meter in service.objects(Meter):
        print(meter.service_location.name)


def get_usage_points(service):
    for ups in service.objects(UsagePoint):
        print(ups)


async def main():
    feeder_mrid = "CPM3B3"
    parser = argparse.ArgumentParser(description="Integration Test of retrieve_network")
    parser.add_argument('server', help='Host and port of grpc server', metavar="host:port", nargs="?",
                        default="ewb.essentialenergy.zepben.com")
    parser.add_argument('--rpc-port', help="The gRPC port for the server", default="9014")
    parser.add_argument('--feeder-mrid', help="The Feeder mRID", default="CPM3B3")
    args = parser.parse_args()
    async with connect_async(host=args.server, rpc_port=args.rpc_port) as channel:
        client = NetworkConsumerClient(channel)
        net = NetworkService()
        (await client.get_feeder(net, mrid=args.feeder_mrid)).throw_on_error()
        print(net.get(feeder_mrid))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
