;(function(){
  exports.sumOf3sAnd5s = sumOf3sAnd5s;

  function sumOf3sAnd5s(n){
    // Sum multiples of 3 and 5 up to the specified number n

    var sum = 0;
    for ( var i = 1; i <= n; i++ ){
      if ( i % 3 == 0 ){
        sum += i;
      }
      if ( i % 5 == 0 && i % 3 != 0 ){
        sum += i;
      }
    }
    return sum;
  }
})();

if (require.main === module) {
  console.log(sumOf3sAnd5s(1000));
}
