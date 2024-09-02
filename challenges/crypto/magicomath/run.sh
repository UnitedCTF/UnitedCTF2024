while :; do
    socat -dd -T300 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:"./bin/python3 challenge.py",stderr
done
