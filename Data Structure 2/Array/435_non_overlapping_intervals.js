/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {
  if (intervals.length == 1) {
    return 0;
  }

  intervals.sort();
  let currentEnd = intervals[0][1];
  let count = 0;

  for (let i = 1; i < intervals.length; i++) {
    console.log(intervals[i]);
    if (intervals[i][0] < currentEnd) {
      count += 1;
      currentEnd = Math.min(currentEnd, intervals[i][1]);
    } else {
      currentEnd = intervals[i][1];
    }
  }

  return count;
};
