# Solution

This is a simple pivoting example. Using proxychains, we can call network command from foothold, through beary, to webserver.

Password: anything1-slander-devourer-registrar

```shell
ssh -D 9050 user@beary
```

Set proxychains configuration file to use sock4 proxy on port 9050.

```shell
sudo echo "socks4 127.0.0.1 9050" >> /etc/proxychains.conf
```

Using the bear's resting area, we can find the network range to scan.

```shell
155: eth0@if156: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP 
    link/ether 02:42:0a:00:00:c3 brd ff:ff:ff:ff:ff:ff
    inet 172.99.53.1/24 brd 172.99.53.255 scope global eth0
       valid_lft forever preferred_lft forever
```

And scan the network range using nmap searching for a website on the ports 80 or 443.

```shell
proxychains nmap 172.99.53.0/24 -sT -p 80,443
```

![alt text](image.png)

```shell
proxychains curl http://172.99.53.183:80
```
