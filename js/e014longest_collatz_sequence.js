/*jshint esversion: 6 */

;(function() {
	exports.collatzSequenceLength = collatzSequenceLength;
	exports.longestCollatzSequence = longestCollatzSequence;

	function collatzSequenceLength(n) {
		// Return the length of the Collatz sequence for n

		// Start with count = 1 because n is part of sequence
		var count = 1,
				currNum = n;
		while (currNum != 1) {
			// currNum is even
			if (currNum % 2 === 0) {  
				currNum /= 2;
				count++;
			}

			// currNum is odd
			else { 
				currNum = (currNum * 3) + 1;
				count++;
			}
		}
		return count;
	}

	function longestCollatzSequence(maxNum) {
		// Return the number with the longest Collatz sequence where number is less
		// than or equal to maxNum

		// Calculate length of Collatz sequence for all numbers up to and including
		// maxNum
		var maxLen = 1,
				ret = 1;

		for (var i = 2; i <= maxNum; i++) {
			var cLen = collatzSequenceLength(i);
			if (cLen > maxLen) {
				ret = i;
				maxLen = cLen;
			}
		}

		return ret
	}  // end of longestCollatzSequence

	if (require.main === module) {
		var numWithLongestCollatz = longestCollatzSequence(1000000);
		console.log('Num with longest: %d, with Collatz sequence length of: %d',
				numWithLongestCollatz, collatzSequenceLength(numWithLongestCollatz));
	}
})();

