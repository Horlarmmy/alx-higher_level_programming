#!/usr/bin/nodelet i = parseInt(process.argv[2]);
if (i == NaN) {
  console.log("Missing size");
} else {
  for (let x = 0; x < i; x++ ){
    console.log("X".repeat(i));
  }
}
