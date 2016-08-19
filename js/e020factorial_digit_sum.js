/**
 * Project Euler Problem #20: Factorial Digit Sum
 */

;(function(){
	exports.factorialDigitSum = factorialDigitSum;

	/**
	 * Given n, sum the digits resulting from n!
	 *
	 * @param {number} n
	 *
	 * @return {number}
	 */
	function factorialDigitSum(n) {
		var bigInt = require('big-integer');
		var digitSum = 0;
		var digitString = '1';
		for (var i = 1; i <= n; i++) {
			digitString = bigInt(digitString).multiply(i).toString();
		}
		for (var j = 0; j < digitString.length; j++) {
			digitSum += parseInt(digitString[j]);
		}
		return digitSum;
	}

	
	if (require.main === module) {
		n = 100;
		console.log('The sum of the digits resulting from '+n+'! is: '+factorialDigitSum(n));
	}
})();

