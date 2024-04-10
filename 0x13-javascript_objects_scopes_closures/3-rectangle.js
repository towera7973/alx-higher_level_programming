#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0)
	  { 
		  [this.width, this.height] = [w, h];
	  }
  }

  print () {
    for (let i = 0; i < this.height; i++)
	  console.log('X'.repeat(this.width));
  }
};
