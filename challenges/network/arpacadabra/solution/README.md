# Solution

Connect with SSH to the attacker box.

The name and description of the challenge strongly indicate that we should perform an ARP poisoning attack. Since we have access to the docker-compose.yml file, we can assume that we need to redirect the requests.

Looking at the webserver, we can see a login page and a flag endpoint that is authenticated. The webserver runs on HTTP.

Googling "ARP poisoning python" provides multiple options, such as the one in solve.py.

We can modify the script to include the IP addresses or the names using Docker Compose's default DNS. We can automatically connect to the webserver, or we can also do it manually.

Run the Python script solve.py. This will perform an ARP poisoning attack, which will redirect the requests from the user to us. Then we can read the flag.

```bash
sudo python solve.py
```

This challenge was strongly inspired by https://github.com/moospit/net-sec-lab/tree/main.
