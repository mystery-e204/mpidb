#!/usr/bin/env python3

import sys
import signal
from options import Options

def construct_formatter(options):
    numDebugRanks = -1
    numInfoReceived = 0
    formatter = None
    info_buffer = []

    for line in sys.stdin:
        words = line.split()
        try:
            rank = int(words[0].partition("mpidb(")[2].partition("):")[0])
        except ValueError:
            sys.stdout.write(line)
            continue

        if rank == 0 and formatter == None:
            appName = words[1]
            numDebugRanks = int(words[2])
            formatter = options.formatter(options.config_name, appName)

            for t in info_buffer:
                formatter.add_rank_info(*t)
        else:
            host = words[1]
            port = int(words[2])
            numInfoReceived += 1
            if formatter:
                formatter.add_rank_info(rank, host, port)
            else:
                info_buffer.append((rank, host, port))

        if numInfoReceived == numDebugRanks and formatter != None:
            break
    
    return formatter


def handleInterrupt(sig, frame):
    sig_name = "UNKNOWN"
    if sig == signal.SIGINT: sig_name = "SIGINT"
    if sig == signal.SIGABRT: sig_name = "SIGABRT"
    sys.exit("Caught signal " + sig_name)


def main():
    signal.signal(signal.SIGINT, handleInterrupt)
    signal.signal(signal.SIGABRT, handleInterrupt)

    options = Options()
    
    with open(options.file_name, "w") as conf_file:
        construct_formatter(options).write_config(conf_file)

    for line in sys.stdin:
        sys.stdout.write(line)


if __name__ == "__main__":
    main()