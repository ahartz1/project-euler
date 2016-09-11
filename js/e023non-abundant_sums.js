/**
 * Project Euler Problem #23: Non-Abundant Sums
 *
 * From the description:
 * "A perfect number is a number for which the sum of its proper divisors is
 * exactly equal to the number. A number n is called deficient if the sum of
 * its proper divisors is less than n and it is called abundant if this sum
 * exceeds n.
 *
 * By mathematical analysis, it can be shown that all integers greater than
 * 28123 can be written as the sum of two abundant numbers.
 *
 * Find the sum of all the positive integers which cannot be written as the sum
 * of two abundant numbers."
 */

;(function(){
	exports.properDivisorSum = properDivisorSum;
	exports.nonAbundantSums  = nonAbundantSums;

	/**
	 * Given n, return the sum of its proper divisors.
	 *
	 * @param {number} n
	 *
	 * @return {number}
	 */
	function properDivisorSum(n) {
		var sum = 0;
		for (var i = 0; i < n; i++) {
			if (n % i === 0) {
				sum += i;
			}
		}
		return sum;
	}

	/**
	 * Return the sum of all numbers that cannot be expressed as the sum of two
	 * abundant numbers.
	 *
	 * @param {number=} max Calculate the sum for n up to this max
	 * @param {boolean=} showConsecutiveStart Output start of consecutive
	 *     numbers that can be expressed as the sum of two abundant numbers?
	 *
	 * @return {number}
	 */
	function nonAbundantSums(max, showConsecutiveStart) {
		var sum           = 0;
		var abundantList  = [];
		var sumOfAbundant = [];
		var stopSearch    = false;
		max = max || 28123;
		max = 0 < max ? max : 28123;
		for (var i = 0; i <= max; i++) {
			addToSum = true;
			for (var j = 0; j < abundantList.length - 1; j++) {
				stopSearch = false;
				for (var k = 1; k < abundantList.length; k++) {
					if (abundantList[j] + abundantList[k] < i) {
						// abundantList[k] too small; try next k
						continue;
					} else if (abundantList[j] + abundantList[k] > i) {
						// abundantList[k] is too big; start next j cycle
						break;
					} else if (abundantList[j] + abundantList[k] === i) {
						// i is the sum of two abundant numbers; do not include
						addToSum = false;
						stopSearch = true;
						sumOfAbundant.push(i);
						break;
					}
				}
				if (stopSearch) {
					// We found two abundant numbers that sum to i
					break;
				}
			}
			if (addToSum) {
				sum += i;
			}

			// If i itself is abundant, add to list
			if (i < properDivisorSum(i)) {
				abundantList.push(i);
			}
		}

		// Let's find the actual beginning of consecutive numbers that are sums
		// of abundant numbers
		if (max >= 28123 && showConsecutiveStart) {
			var consecutive = [];
			for (var l = sumOfAbundant.length - 1; l > 1; l--) {
				if (sumOfAbundant[l] === sumOfAbundant[l - 1] + 1) {
					consecutive.unshift(sumOfAbundant[l - 1]);
				} else {
					break;
				}
			}
			console.log('The beginning of consecutive numbers that are sums of abundant numbers: '+consecutive[0]);
		}
		return sum;
	}

	
	if (require.main === module) {
		console.log('The sum of all numbers that cannot be expressed as the sum of two abundant numbers: '+nonAbundantSums(28123, true));
	}
})();

