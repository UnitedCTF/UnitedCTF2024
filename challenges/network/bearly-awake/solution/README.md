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

```shell
proxychains nmap 172.99.53.0/24 -sT -p 80
```

![alt text](image.png)

```shell
proxychains curl http://172.99.53.183:80
```
