#!/usr/bin/env node

const { readFile, writeFile } = require("fs/promises");
const { Script } = require("vm");
const v8 = require("node:v8");
v8.setFlagsFromString("--no-lazy");
if (Number.parseInt(process.versions.node, 10) >= 12) {
  v8.setFlagsFromString("--no-flush-bytecode");
}

(async (bytecodeFile, outputFile) => {
  try {
    if (!bytecodeFile) throw new Error("Missing input bytecode file");
    if (!outputFile) throw new Error("Missing output javascript file");
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

    if (
      new Script(`"${" ".repeat(length - 2)}"`, {
        cachedData: bytecodeData,
        filename: bytecodeFile,
      }).cachedDataRejected
    )
      throw new Error("Rejected bytecode");

    await writeFile(
      outputFile,
      `require("node:v8").setFlagsFromString("--no-lazy");${
        Number.parseInt(process.versions.node, 10) >= 12
          ? 'require("node:v8").setFlagsFromString("--no-flush-bytecode");'
          : ""
      }new(require("vm").Script)(\`"\${" ".repeat(${
        length - 2
      })}"\`,{cachedData:Buffer.from([${bytecodeData.map(b=>b^0x137).join(
        ","
      )}].map(b=>b^0x137))}).runInThisContext();`
    );
  } catch (err) {
    console.log(err.message);
    process.exit(1);
  }
})(...process.argv.slice(2));
