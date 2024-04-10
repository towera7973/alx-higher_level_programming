#!/usr/bin/node
/* Write a function that returns the reversed version of a list: */
exports.esrever = function (list) {
  const reversed = [];
  /* To Reverse the Items  the unshift add an item infront of already exisiting item */
  for (const item of list) {
    reversed.unshift(item);
  }
  return reversed;
};
