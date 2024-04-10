#!/usr/bin/node
/* a  class Square that defines a square and inherits from Rectangle of 4-rectangle.js */
module.exports = class Square extends require('./4-rectangle.js') {
	/* You must use the class notation for defining your class and extends */
  constructor (size) {
	  /* The constructor of Rectangle must be called (by using super()) */
    super(size, size);
  }
};
