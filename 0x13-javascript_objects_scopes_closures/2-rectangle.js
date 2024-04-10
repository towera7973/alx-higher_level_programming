#!/usr/bin/node
/* Write a class Rectangle that defines a rectangle - If w or h is equal to 0 or not a positive integer, create an empty object */
module.exports = class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) { [this.width, this.height] = [w, h]; }
  }
};
