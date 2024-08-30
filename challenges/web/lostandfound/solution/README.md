# Lost and found 🎈

## Write-up

By enumerating the website a little, we can see that the directory `/.git` is disallowed in the `/robots.txt` file. Luckily for us, since we are not robots, we can use a tool such as `git-dumper` to download the whole `.git` folder to our local computer.

From there, we can see that there are only two commit by using the command `git log`.

```git
commit 554950181c66c61d2425de4c218f1d3896e9069a (HEAD -> main)
Author: John Doe <jdoe@circus.local>
Date:   Thu Aug 29 23:12:28 2024 -0400

    Lost balloon

commit 228d792323327bdf9078deac272f40b7c88e7db8
Author: John Doe <jdoe@circus.local>
Date:   Thu Aug 29 23:10:43 2024 -0400

    Initial commit
```

But it is not the only command at our disposition. We can also use the command `git reflog` to view all the reference logs.

```
5549501 (HEAD -> main) HEAD@{0}: rebase (finish): returning to refs/heads/main
5549501 (HEAD -> main) HEAD@{1}: commit: Lost balloon
228d792 HEAD@{2}: rebase (start): checkout 228d792323327bdf9078deac272f40b7c88e7db8
1214731 HEAD@{3}: commit: Lost balloon
1a8c97a HEAD@{4}: commit: Gave balloon
228d792 HEAD@{5}: commit (initial): Initial commit
```

We can see that there was a commit named `Gave balloon` but it was overwritten by a rebase.

We can return to that lost commit by running the command `git checkout 1a8c97a`.

Timmy now has his balloon back and the flag can be found next to him in the file `index.html`

## Flag

`flag-n0th1ng1sl0st1nr3fl0g`
