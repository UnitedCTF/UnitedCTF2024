#!/usr/bin/env node

const { extname } = require("path");
const { readFile, writeFile } = require("fs/promises");
const { Script } = require("vm");
const v8 = require("node:v8");
v8.setFlagsFromString("--no-lazy");
if (Number.parseInt(process.versions.node, 10) >= 12) {
  v8.setFlagsFromString("--no-flush-bytecode");
}

(async (javascriptFile) => {
  try {
    if (!javascriptFile) throw new Error("Missing input javascript file");
    const javascriptCode = (await readFile(javascriptFile))
      .toString()
      .replace(/^#!,*/g, "");
    const cachedData = new Script(javascriptCode).createCachedData();
    await writeFile(
      javascriptFile.slice(0, -extname(javascriptFile).length) + ".jsc",
      cachedData
    );
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
})(...process.argv.splice(2));
