# Escape room 0

## Write-up

There is no filter, but `require` is not defined in the `eval` context. You can access the `require` function by calling `process.mainModule.require` instead.

## Flag

`flag-6e9e2e450d06b87f7bf73cb0a4d4c75d`
