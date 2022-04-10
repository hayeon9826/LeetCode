"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the 'solution' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER X
 *  2. INTEGER_ARRAY arr
 *  3. INTEGER_ARRAY indexes
 */

function solution(X, arr, indexes) {
  let x_index = [];
  let answer = [];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == X) x_index.push(i);
  }

  for (let i = 0; i < indexes.length; i++) {
    if (indexes[i] <= x_index.length) {
      answer.push(x_index[indexes[i] - 1] + 1);
    } else {
      answer.push(-1);
    }
  }

  return answer;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const X = parseInt(readLine().trim(), 10);

  const arrCount = parseInt(readLine().trim(), 10);

  let arr = [];

  for (let i = 0; i < arrCount; i++) {
    const arrItem = parseInt(readLine().trim(), 10);
    arr.push(arrItem);
  }

  const indexesCount = parseInt(readLine().trim(), 10);

  let indexes = [];

  for (let i = 0; i < indexesCount; i++) {
    const indexesItem = parseInt(readLine().trim(), 10);
    indexes.push(indexesItem);
  }

  const result = solution(X, arr, indexes);

  ws.write(result.join("\n") + "\n");

  ws.end();
}
