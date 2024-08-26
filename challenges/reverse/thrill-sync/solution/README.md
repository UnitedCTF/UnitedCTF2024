# Solution

## Flag 1

We can export the hashes from the database. Then try to crack the hash using hashcat and rockyou.txt.

```python
import sqlite3

def read_users():
    db = sqlite3.connect("thrill-sync.db")
    sql = "SELECT password FROM users"
    hashes = db.execute(sql).fetchall()
    db.close()
    with open("hash.txt", "w") as f:
        f.write("\n".join([hash[0] for hash in hashes]))
```

```shell
hashcat -a 0 -m 1400 hash.txt rockyou.txt

cac5fe440a4ee9d61387f8f39c5c76c61c1393c886490bb64e2249fc862944de:425kailua
```

![hashcat.png](hashcat.png)

Then we can connect and get the flag using the client or `solve_1.py`.

## Flag 2

We can see that the server uses session token to keep track of a logged session. There might be a token that is still valid. Using `solve_2.py`, we try every token and get a hit.

## Flag 3

Looking through the hashes and knowing from the challenge description that the server is in PHP, we can see EthanClark hash is a magic hash. If the server uses a loose comparaison between hashes, any password that hash to a magic hash will be valid to login. See https://github.com/spaze/hashes.

This repo has example of magic hash for sha256: https://github.com/spaze/hashes/blob/master/sha256.md

We can then use `solve_3.py` to get the last flag.
