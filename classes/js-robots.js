// Javascript does not natively have Classes, but it has prototyping

class Robot {
  constructor(name, color, weight) {
    this.name = name;
    this.color = color;
    this.weight = weight;
  }
  introduce_self() {
    console.log(
      'Domo arrigato I am Mrs Roboto ' +
        this.name +
        ', I am ' +
        this.color +
        ' and weigh ' +
        this.weight +
        ' kilos.'
    );
  }
}

// the 'new' keyword
// - 1. creates a new empty object
// - 2. sets the value of 'this' to be the new empty object
// - 3. calls the constructor method

var r1 = new Robot('Anya', 'Green', 34);
var r2 = new Robot('Karla', 'Teal', 23);
console.log(r1);
console.log(r2);

r1.introduce_self();
r2.introduce_self();
