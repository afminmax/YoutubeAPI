// Javascript does not natively have Classes, but it has prototyping

class Robot {
  constructor(name, color, weight) {
    this.name = name;
    this.color = color;
    this.weight = weight;
  }
}

var r1 = new Robot('Anya', 'Green', 34);
var r2 = new Robot('Karla', 'Teal', 23);
console.log(r1);
console.log(r2);

// the 'new' keyword
// - 1. creates a new empty object
// - 2. sets the value of 'this' to be the new empty object
// - 3. calls the constructor method
