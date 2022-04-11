#!/usr/bin/python3

import socket
import sys

sys_name=socket.gethostbyname('www.amazon.com')
ip_addr=socket.gethostbyname(sys_name)
print(ip_addr)
