# Man in the middle

A project just for study about Man in the Middle attack

## Premise

Everytime we connect any website the request will go through a `gateway` to come the website.

## How the man in the middle concept works:

Suppose I'm connected in the public network, I need:

1. Tell the gateway that I'm the proxy
2. Tell the victim that I'm the gateway

Now I'm in the middle between the victim and the gateway!

## What we need?

1. List all IPs connected in the same network

```
sudo python3 ips_mapper.py
```
