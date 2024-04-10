#!/usr/bin/node
/*  a function that converts a number from base 10 to another base passed as argument */
exports.converter = function (base) {
  return function (number) {
    /* The toString() method converts a number to a string. 2-binary, 8-octal, 16-haxa */
    return number.toString(base);
  };
};
