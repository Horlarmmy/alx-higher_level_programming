#!/usr/bin/node
const i = parseInt(process.argv[2]);
if (Number.isNaN(i)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < i; x++) {
    console.log('X'.repeat(i));
  }
}
