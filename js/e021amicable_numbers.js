/**
 * Project Euler Problem #21: Amicable Numbers
 *
 * From description:
 * "Let d(n) be defined as the sum of proper divisors of n (numbers less than n
 * which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a
 * and b are an amicable pair and each of a and b are called amicable numbers."
 *
 * Find the sum of amicable numbers up to m.
 */

;(function(){
	exports.divisorSum = divisorSum;
	exports.isAmicable = isAmicable;
	exports.amicableNumberSum = amicableNumberSum;

	/**
	 * Given n, return the sum of its divisors.
	 *
	 * @param {number} n
	 *
	 * @return {number}
	 */
	function divisorSum(n) {
		var sum = 0;
		for (var i = 0; i < n; i++) {
			if (n % i === 0) {
				sum += i;
			}
		}
		return sum;
	}

	/**
	 * If the input number is a part of an amicable pair, return its pair.
	 * Otherwise, return false.
	 * 
	 * @param {number} a
	 *
	 * @return {number|boolean}
	 */
	function isAmicable(a) {
		var b = divisorSum(a);
		if (a === divisorSum(b) && a !== b) {
			return b;
		}
		return false;
	}

	/**
	 * Given n, return the sum of all amicable numbers below n.
	 *
	 * @param {number} n
	 *
	 * @return {number}
	 */
	function amicableNumberSum(n) {
		var amicableSum = 0;
		var candidate = 0;
		for (var i = 1; i < n; i++) {
			candidate = isAmicable(i);
			if (candidate !== false) {
				amicableSum += i;
			}
		}
		return amicableSum;
	}

	
	if (require.main === module) {
		n = 10000;
		console.log('The sum of amicable numbers up to '+n+' is: '+amicableNumberSum(n));
	}
})();

