#!/usr/bin/node
exports.converter = function (base) {
  return function (argument) {
    return argument.toString(base);
  };
};
