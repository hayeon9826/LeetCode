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
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY infectedHouses
 */

function solution(n, infectedHouses) {
  // Write your code here
  let answer = new Array(n).fill(0);
  let count = 1;
  let elemCount = 0;
  // initial setting
  for (let i = 0; i < infectedHouses.length; i++) {
    answer[infectedHouses[i] - 1] = 1;
  }

  let answer_copy = JSON.parse(JSON.stringify(answer));

  // check house
  for (let i = 0; i < n; i++) {
    if (answer.reduce((a, b) => a + b, 0) == n) break;
    // check virus

    for (let j = 0; j < answer.length; j++) {
      if (answer[j] == 1) {
        if (j > 0 && answer_copy[j - 1] != 1) {
          answer_copy[j - 1] = 1;
          elemCount += 1;
        }
        if (j < n - 1 && answer_copy[j + 1] != 1) {
          answer_copy[j + 1] = 1;
          elemCount += 1;
        }
      }
    }

    count = count * factorial(elemCount);
    answer = JSON.parse(JSON.stringify(answer_copy));
    elemCount = 0;
  }

  return count % 10000000007;
}

function factorial(number) {
  let result = 1;
  for (let i = 2; i <= number; i++) {
    result = result * i;
  }

  return result;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine().trim(), 10);

  const infectedHousesCount = parseInt(readLine().trim(), 10);

  let infectedHouses = [];

  for (let i = 0; i < infectedHousesCount; i++) {
    const infectedHousesItem = parseInt(readLine().trim(), 10);
    infectedHouses.push(infectedHousesItem);
  }

  const result = solution(n, infectedHouses);

  ws.write(result + "\n");

  ws.end();
}
