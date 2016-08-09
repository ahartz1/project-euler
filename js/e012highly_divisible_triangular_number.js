;(function() {
  exports.triangularDivisors = triangularDivisors;

  function triangularDivisors(n) {
		// Return first triangular number with *more than* n divisors
		// Triangular number is a number in sequence of 1 + 2 + 3 + 4 + 5 + ...

		// Strategy for solving: keep track of current triangular number, check for
		// number of divisors, if less than n, produce the next triangular number to
		// check and repeat

		var checkNumFactors = function (curr_tri) {
			var numFactors = 0;
			for (var i = 1; i <= curr_tri; i++) {
				if (curr_tri % i === 0) {
					numFactors++;
				}
			}
			return numFactors <= n;
		};

		var index = 1,
				tri = 1;
		while (checkNumFactors(tri)) {
			index++;
			tri += index;
		}
		return tri;
	}  // end of triangularDivisors

	if (require.main === module) {
		console.log('For n of 500, answer = 76576500 (took ~30 min to calculate!)');
	}
})();

