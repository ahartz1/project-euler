/**
 * Project Euler Problem #22: Names Scores
 *
 * Read in the names in the file, alphabetize them. Calculate the alphabetical
 * value of each name and multiply it by its position in the name list. Return
 * the sum of these values.
 */

;(function(){
	exports.namesScoresSum  = namesScoresSum;
	exports.alphabeticalSum = alphabeticalSum;

	/**
	 * Given a names file, parse the names and return it as a sorted list.
	 *
	 * @param {string} filepath
	 *
	 * @return {Array.<string>}
	 */
	function processNamesFile(filepath) {
		var nameList = [];

		// Get access to FileSystem functions with fs
		var fs = require('fs');

		// Get access to the file contents
		var contents = fs.readFileSync(filepath, 'utf8');

		// Parse names
		var names = contents.split(',');
		for (var i = 0; i < names.length; i++) {
			// Remove quotes surrounding names
			nameList[i] = names[i].replace(/"/g, '');
		}
		return nameList.sort();
	}

	/**
	 * Given a word, return its alphabetical sum.
	 *
	 * @param {string} word
	 *
	 * @return {number}
	 */
	function alphabeticalSum(word) {
		var sum = 0;
		// Make word lowercase with no extra surrounding whitespace
		word = word.toLowerCase().trim();
		for (var i = 0; i < word.length; i++) {
			// The lowercase latin alphabet starts at 97 in unicode, so
			// subtract 96 to get value
			sum += word.charCodeAt(i) - 96;
		}
		return sum;
	}

	/**
	 * Given filepath, return the sum of the names scores.
	 *
	 * @param {string} filepath
	 *
	 * @return {number}
	 */
	function namesScoresSum(filepath) {
		// Get sorted names array from file
		var nameList = processNamesFile(filepath);

		var sum     = 0;
		var nameSum = 0;
		for (var i = 0; i < nameList.length; i++) {
			nameSum = alphabeticalSum(nameList[i]);

			// Multiply the alphabetical sum by the name's position in the list
			sum += nameSum * (i + 1);
		}
		return sum;
	}

	
	if (require.main === module) {
		filepath = 'data/p022_names.txt';
		console.log('The sum of name scores in '+filepath+' is: '+namesScoresSum(filepath));
	}
})();

