# Security through obskurity

## Write-up (français)

## Write-up (english)

The intended way to solve this challenge is to ignore most of it. You very well could try and understand it all, but as the description implies, you don't need to. It's a waste of time: over 60% of the code is used to calculate a constant array (`s`) you can simply copy-paste into your solution with no worry.

I'll assume you know how the basics of reading K from [the tutorial linked in the description](https://razetime.github.io/ngn-k-tutorial/), but as a short summary:
- with a few exceptions, everything is executed and read from right to left
- `a:b` is variable assignment (`a = b` in other languages)
- `{}` makes a function
- `f[a;b]` calls function `f` with arguments `a` and `b`

The meat of the algorithm is the last line: `0{s@e[x;y]}\"flag-redacted"`. Unlike every other line, this isn't an assignment, and thus it prints its result. It's what gives us the ciphertext.

Looking at the manual, we can see multiple definitions of `\`. Seeing as there's `0` on the left of the function, and the function uses 2 implicit arguments (`x` and `y`) which makes it "dyadic", we're looking at `x F\`, a "seeded scan".

Thus, we can say that knowing `x`, the last character of the ciphertext, `s@e[x;y]` encrypts one character `y`. Going from right to left as usual, the next function to look at is `e:b/~=/b\',`, which is equivalent to `e:{b/~=/b\'x,y}`.

`e` first puts its arguments into a two-element list using `,`, then encodes (`\`) each (`'`) to binary (because `b` is defined as `8#2`, a 8-element list filled with 2). We can alreay see `b/` which decodes back (no each, a single result!) from binary. From `~` (not) and `=` (equals), you can hopefully guess this function is the `e`xclusive or bitwise operator.

The last part of our "encryption" algorithm then is `s`. As aforementioned, you aren't supposed to try to understand this part. If you try and evaluate `s`, and maybe `#s`, you'll see it's a 256-element list containing the integers from 0 to 255. It's a permutation, or in other words, a **substitution box**. To decrypt then, we won't need to know how `s` was calculated, we'll simply need to invert the permutation.

We can finally mathematically describe our algorithm as follows:
$$e_i = S(m_i \oplus e_{i-1})$$

And solving for our plaintext $m$:
$$\begin{align*}
m_i &= m_i \oplus 0
\\&= m_i \oplus (e_{i-1} \oplus e_{i-1})
\\&= S^{-1}(S(m_i \oplus e_{i-1})) \oplus e_{i-1}
\\&= S^{-1}(e_i) \oplus e_{i-1}
\end{align*}$$

All that's left is to write the decryption script. If you're boring there's a python solution [here](decrypt.py), but let's solve it in K for the hell of it.

The most obvious way to invert the S-box would perhaps be to find the index of every value from 0 to 255 (`s?/:!256`) but there is a [more convenient idiom](https://mlochbaum.github.io/BQN/doc/order.html#ordinals) to invert a permutation in array languages like K; you just need to sort: `<s`.

Array indexing `@` allows us to get the values at multiple indicies at once, so `(<s)@encrypted` will pass the entire ciphertext through the inverse S-box at once. Next, shift the ciphertext and add a zero: `0,-1_encrypted`. We can reuse the `e` function we already have for xor. `(0,-1_encrypted)e'(<s)@encrypted` is all it takes to decrypt.

...but unless you know the ASCII table by heart, the real last step will be to cast the list of bytes to a string:

```
`c$(0 :':encrypted)e'(<s)@encrypted
```

## Flag

`flag-h0peUd1dntR34Dev3erything`
