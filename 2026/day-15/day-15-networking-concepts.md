# Day 15 Networking Concepts

## DNS

- `A`: maps a name to an IPv4 address.
- `AAAA`: maps a name to an IPv6 address.
- `CNAME`: alias to another DNS name.
- `MX`: mail exchanger.
- `NS`: authoritative name server.

## IP Addressing

- Private ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.
- Public IPs are reachable on the internet when routing and firewall rules allow it.

## CIDR Table

| CIDR | Subnet Mask | Total IPs | Usable Hosts |
|------|-------------|-----------|--------------|
| /24  | 255.255.255.0 | 256 | 254 |
| /16  | 255.255.0.0 | 65536 | 65534 |
| /28  | 255.255.255.240 | 16 | 14 |

## Common Ports

| Port | Service |
|------|---------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 53 | DNS |
| 3306 | MySQL |
| 6379 | Redis |
| 27017 | MongoDB |

