#!/usr/bin/env node

const { readFile } = require("fs/promises");
const { Script } = require("node:vm");
const v8 = require("node:v8");
v8.setFlagsFromString("--no-lazy");
if (Number.parseInt(process.versions.node, 10) >= 12) {
  v8.setFlagsFromString("--no-flush-bytecode");
}

(async (bytecodeFile) => {
  try {
    // Remove this script from the args
    process.argv.splice(1, 1);

    if (!bytecodeFile) throw new Error("Missing input bytecode file");
    const bytecodeData = await readFile(bytecodeFile);
    let length;
    if (
      process.version.startsWith("v8.8") ||
      process.version.startsWith("v8.9")
    ) {
      length = bytecodeData
        .subarray(12, 16)
        .reduce(
          (sum, number, power) => (sum += number * Math.pow(256, power)),
          0
        );
    } else {
      length = bytecodeData
        .subarray(8, 12)
        .reduce(
          (sum, number, power) => (sum += number * Math.pow(256, power)),
          0
        );
    }
  
    const script = new Script(`"${" ".repeat(length - 2)}"`, {
      cachedData: bytecodeData,
      filename: bytecodeFile
    });
    if (script.cachedDataRejected) throw new Error("Rejected bytecode");
    return script.runInThisContext();
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
})(...process.argv.slice(2));
