# proc_net_tcp_decoder

This script is designed to format and convert the output of the `/proc/net/tcp` file from hexadecimal to decimal. The file contains information about currently active TCP connections, allowing to identify interfaces along with their respective local and remote IP addresses, as well as their corresponding ports.

## Setup

You'll need to have Python 3 installed on your machine to run the script.

You must update the global variable `data` with the output of the indexes obtained from `/proc/net/tcp` of the target machine.

```bash
data = """
0: 00000000:0016 00000000:0000 0A 00000000:00000000 00:00000000 00000000 0 0 916869924 1 0000000000000000 100 0 0 10 0
1: 0100007F:22B8 00000000:0000 0A 00000000:00000000 00:00000000 00000000 0 0 916871144 1 0000000000000000 100 0 0 10 0
2: 0B00007F:92BB 00000000:0000 0A 00000000:00000000 00:00000000 00000000 65534 0 916899881 1 0000000000000000 100 0 0 10 0
3: 00000000:1F40 00000000:0000 0A 00000000:00000000 00:00000000 00000000 0 0 916898925 1 0000000000000000 100 0 0 10 0
4: 037DB9C0:1F40 027DB9C0:8998 01 00000000:00000000 00:00000000 00000000 0 0 916989497 1 0000000000000000 20 4 30 10 -1
5: 037DB9C0:1F40 027DB9C0:8994 06 00000000:00000000 03:0000176E 00000000 0 0 0 3 0000000000000000
"""
```

## Output Example

```python
Connection Serial Number: 0
Local Address: 0.0.0.0:22
Remote Address: 0.0.0.0:0
State: 0A
TX Queue: 00000000:00000000
RX Queue: 00:00000000
Traffic: 00000000
Time When: 0
Retransmit: 0
UID: 916869924
Timeout: 1
INode: 0000000000000000
-----------------------------
Connection Serial Number: 1
Local Address: 127.0.0.1:8888
Remote Address: 0.0.0.0:0
State: 0A
TX Queue: 00000000:00000000
RX Queue: 00:00000000
Traffic: 00000000
Time When: 0
Retransmit: 0
UID: 916871144
Timeout: 1
INode: 0000000000000000
-----------------------------
Connection Serial Number: 2
Local Address: 127.0.0.11:37563
Remote Address: 0.0.0.0:0
State: 0A
TX Queue: 00000000:00000000
RX Queue: 00:00000000
Traffic: 00000000
Time When: 65534
Retransmit: 0
UID: 916899881
Timeout: 1
INode: 0000000000000000
-----------------------------
Connection Serial Number: 3
Local Address: 0.0.0.0:8000
Remote Address: 0.0.0.0:0
State: 0A
TX Queue: 00000000:00000000
RX Queue: 00:00000000
Traffic: 00000000
Time When: 0
Retransmit: 0
UID: 916898925
Timeout: 1
INode: 0000000000000000
-----------------------------
Connection Serial Number: 4
Local Address: 192.185.125.3:8000
Remote Address: 192.185.125.2:35224
State: 01
TX Queue: 00000000:00000000
RX Queue: 00:00000000
Traffic: 00000000
Time When: 0
Retransmit: 0
UID: 916989497
Timeout: 1
INode: 0000000000000000
-----------------------------
Connection Serial Number: 5
Local Address: 192.185.125.3:8000
Remote Address: 192.185.125.2:35220
State: 06
TX Queue: 00000000:00000000
RX Queue: 03:0000176E
Traffic: 00000000
Time When: 0
Retransmit: 0
UID: 0
Timeout: 3
INode: 0000000000000000
-----------------------------
```
