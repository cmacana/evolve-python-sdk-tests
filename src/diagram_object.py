import getopt
from sys import argv

import zepben.evolve as cim
from zepben.evolve import connect_async, ProducerClient
import geopandas as gp
from tkinter import filedialog
from tkinter import *
from pathlib import Path
import logging
import asyncio
import argparse
import pydash
import json
import os

# TODO: Support creation of DiagramObjects and add to a Diagram Service such that the can be visualized in the Network Map
# The cimbend libary is generating a error with self.diagram.add_object(do)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def createNetwork():
    ds = cim.DiagramService()
    ns = cim.NetworkService()
    diagram = cim.Diagram(diagram_style=cim.DiagramStyle.GEOGRAPHIC)
    eq = cim.PowerTransformer()
    do = cim.DiagramObject(diagram=diagram, identified_object_mrid=eq.mrid,
                           style=cim.DiagramObjectStyle.DIST_TRANSFORMER)
    diagram.add_object(do)
    ds.add(do)
    ds.add(diagram)
    ns.add(eq)
    return [ns, ds]


async def main():
    rpc_port = 50051
    host = "localhost"
    try:
        opts, args = getopt.getopt(argv, "h:i:p:u:", ["mrid=", "port=", "host="])
    except getopt.GetoptError:
        print('get_feeder.py -i <feeder_mrid> -p <rpc_port> -u <host>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('get_feeder.py -p <rpc_port> -i <feeder_mrid>')
            sys.exit()
        elif opt in ("-i", "--mrid"):
            feeder_mrid = arg
        elif opt in ("-p", "--port"):
            rpc_port = arg
        elif opt in ("-u", "--host"):
            host = arg

    # Creates a Network
    network = createNetwork()

    async with connect_async(host=host, rpc_port=rpc_port) as channel:
        # Send the network to the postbox instance.
        client = ProducerClient(channel)
        # Send the network to the postbox instance.
        res = await client.send(network)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

