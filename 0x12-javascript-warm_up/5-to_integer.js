#!/usr/bin/nodeif (process.argv[2] === undefined) {
  console.log('Not a number');
  } else if (Number.isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log(parseInt(process.argv[2]));
}
