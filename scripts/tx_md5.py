#!/usr/bin/env python

import PacketTX, sys, os, argparse, logging
from radio_wrappers import *

def transmit_file(filename, tx_object):
    file_size = os.path.getsize(filename)
    if file_size % 256 > 0:
        print("File size not a multiple of 256 bytes!")
        return

    print("Transmitting %d Packets." % (file_size // 256))
    with open(filename, 'rb') as f:
        for _ in range(file_size // 256):
            data = f.read(256)
            tx_object.tx_packet(data)
    print("Waiting for tx queue to empty...")
    tx_object.wait()

parser = argparse.ArgumentParser()
parser.add_argument("--rfm98w", default=None, type=int, help="If set, configure a RFM98W on this SPI device number.")
parser.add_argument("--frequency", default=443.500, type=float, help="Transmit Frequency (MHz). (Default: 443.500 MHz)")
parser.add_argument("--baudrate", default=115200, type=int, help="Wenet TX baud rate. (Default: 115200).")
parser.add_argument("--serial_port", default="/dev/ttyAMA0", type=str, help="Serial Port for modulation.")
parser.add_argument("--tx_power", default=17, type=int, help="Transmit power in dBm (Default: 17 dBm, 50mW. Allowed values: 2-17)")
parser.add_argument("directory", type=str, help="Directory containing files to checksum and transmit.")
args = parser.parse_args()

logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.DEBUG if args.verbose else logging.INFO)

if args.rfm98w is None:
    logging.critical("No radio type specified! Exiting")
    sys.exit(1)

radio = RFM98W_Serial(
    spidevice=args.rfm98w,
    frequency=args.frequency,
    baudrate=args.baudrate,
    serial_port=args.serial_port,
    tx_power_dbm=args.tx_power
)

tx = PacketTX.PacketTX(radio=radio, udp_listener=55674)
tx.start_tx()

try:
    # Generate MD5 checksums and save to a text file
    checksum_file = "md5sums.txt"
    print(f"\nTXing: {checksum_file}")
    transmit_file(checksum_file, tx)
finally:
    print("Closing transmission.")
    tx.close()