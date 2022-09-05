#!/bin/node
if (process.argv[2] === undefined) {
  console.log('Not a number');
}
  else if (parseInt(process.argv[2] === NaN)) {
  console.log('Not a number');
} else {
  console.log(parseInt(process.argv[2]));
}
