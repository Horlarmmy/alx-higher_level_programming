#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
    }
  }
  
  double() {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
  
  rotate() {
    x = this.width;
    this.width = this.height;
    this.height = x;
  }
  
  print() {
    for (var i = 0; i < height.length; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
