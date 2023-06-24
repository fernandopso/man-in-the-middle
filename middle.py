#!/usr/bin/env python3

import time

GATEWAY = "192.168.0.1";

class Middle(object):
    def __init__(self) -> None:
        print("setup configs to the man in the middle");

        self.arp = ""
        self.http = ""
        self.ftp = ""
        self.gateway = ""
        self.targets = ""
        self.dns = ""
        self.captive = ""
        self.captive_dir = ""
        self.captive_ip = ""

        pass

    def _arp(self):
        if self.arp:
            ARPPoison(targets=self.targets,gateway=self.gateway).start()

    def kill(self):
        print("kill the man");

if __name__ == "__main__":
    gmidle = Middle();
    try:
        while True:
            print("running every second");
            # Sending packets every second to guarantees the device immediately
            # overwrite the route to gateway and think that we the gateway
            time.sleep(0.1)
    except KeyboardInterrupt:
        gmidle.kill();
