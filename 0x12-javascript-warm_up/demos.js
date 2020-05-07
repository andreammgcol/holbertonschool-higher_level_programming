function add(){
    console.log('holaaaaaa')
}

add();



var numbers = [4, 2, 5, 1, 3];
numbers.sort(function(a, b) {
  // return a - b;
  return b - a;
});
console.log(numbers);

// [1, 2, 3, 4, 5]