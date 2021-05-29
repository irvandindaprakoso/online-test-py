function getPrimes(value) {
  var result = [];

  for(var i = 0; i < value; i++) { //4
    if (i>1) {
      for(var j = 2; j < i; j++) {
        if(i % j == 0) {
          break;
        }
      }
      result.push(i);
    }
  }
  console.log(result);
}

getPrimes(10);