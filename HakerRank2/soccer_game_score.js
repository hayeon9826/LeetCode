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
 *  1. INTEGER_ARRAY teamK
 *  2. INTEGER_ARRAY teamB
 */

function solution(teamK, teamB) {
  let answer = [];
  teamK.sort((a, b) => a - b);

  for (let i = 0; i <= teamB.length; i++) {
    for (let j = teamK.length - 1; j >= 0; j--) {
      if (teamK[0] > teamB[i]) {
        answer.push(0);
        break;
      }
      if (teamB[i] >= teamK[j]) {
        answer.push(j + 1);
        break;
      }
    }
  }

  return answer;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const teamKCount = parseInt(readLine().trim(), 10);

  let teamK = [];

  for (let i = 0; i < teamKCount; i++) {
    const teamKItem = parseInt(readLine().trim(), 10);
    teamK.push(teamKItem);
  }

  const teamBCount = parseInt(readLine().trim(), 10);

  let teamB = [];

  for (let i = 0; i < teamBCount; i++) {
    const teamBItem = parseInt(readLine().trim(), 10);
    teamB.push(teamBItem);
  }

  const result = solution(teamK, teamB);

  ws.write(result.join("\n") + "\n");

  ws.end();
}
