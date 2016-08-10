/**
 * Project Euler Problem #17: Maximum Path Sum I
 *
 * The goal here is to find the largest possible sum along a path of numbers
 * arranged into a triangular array.
 *
 * e.g., for the below triangle: 3 + 7 + 4 + 9 = 23
 *
 *      `3
 *     `7 4
 *    2 `4  6
 *  8  5 `9  3
 */

;(function(){
	exports.maxPathSumI = maxPathSumI;

	/**
	 * We need to look at the surroundings and keep track of the maximum sum
	 * arriving at any single node. Using the above example, if I was on
	 * row[1], I would record the 3 as the maximum path and note that the
	 * maximum sum at positions 0 and 1 were 10 and 7, respectively.
	 *
	 * The record for each position on a new row should include the maximum
	 * path that it took to reach there and the sum represented by that path.
	 * For example, on row[3], the path at position 2 would be: [0] 3, [1] 7,
	 * [2] 4, [3] 9 with a sum of 23.
	 *
	 * For each position, assess which neighbor above has the highest sum. The
	 * path with the highest sum "wins" the slot and records the new position
	 * as part of its path. This way, we know the maximum available sum at any
	 * position, but do not have to maintain all of the paths. We can always
	 * look at the current row and know the maximum sum.
	 *
	 * In the below, the index in main array represents position within a row
	 * and the index in path array represents the row 
	 *
	 * Data structure at row[2]:
	 * [
	 *		{'sum': 12, 'path': [3, 7, 2]},
	 *		{'sum': 14, 'path': [3, 7, 4]},
	 *		{'sum': 13, 'path': [3, 4, 6]}
	 *	]
	 *
	 *	How to calculate the next row?
	 *	Match-ups in relation to working row:
	 *	 * Position x matches with x and x - 1 on row above
	 *	 * If no x or x - 1 exists in above row, take only choice
	 *
	 * Data structure at row[3]:
	 *	[
	 *		{'sum': 20, 'path': [3, 7, 2, 8]},
	 *		{'sum': 19, 'path': [3, 7, 4, 5]},
	 *		{'sum': 23, 'path': [3, 7, 4, 9]},
	 *		{'sum': 16, 'path': [3, 4, 6, 3]}
	 *	]
	 */
	function maxPathSumI(triangle){
		// Main data structure to hold all paths, with index position
		// corresponding to position in row
		var paths = [];

		// Add a new entry to paths when at a right-side edge
		var addEntry = function(sum, path) {
			var entry  = {};
			entry.sum  = parseInt(sum);
			entry.path = path;
			paths.push(entry);
		};

		// Update an existing entry to include the current number
		var updateEntry = function(entry, value, index) {
			paths[index].sum = entry.sum + parseInt(value);
			var tempPath     = JSON.parse(JSON.stringify(entry.path));
			tempPath.push(parseInt(value));
			paths[index].path = tempPath;
		};

		// Placeholder variables
		var updatedPath = [];
		var pathsCopy   = [];

		var rows  = triangle.split("\n");
		for (var i = 0; i < rows.length; i++) {
			rows[i] = rows[i].split(" ");
			if (i === 0) {
				addEntry(rows[i][0], [parseInt(rows[i][0])]);
				continue;
			}
			// Make a deep copy of the existing paths to compare against while
			// we change paths
			pathsCopy = JSON.parse(JSON.stringify(paths));
			for (var j = 0; j < rows[i].length; j++) {
				// Compare at sum at position - 1 and position in row above
				var posA = (typeof pathsCopy[j - 1] != 'undefined') ? pathsCopy[j - 1] : 0;
				var posB = (typeof pathsCopy[j]     != 'undefined') ? pathsCopy[j]     : 0;
				
				if (posA === 0 || posA.sum < posB.sum) {
					updateEntry(posB, rows[i][j], j);
				} else if (posA.sum > posB.sum) {
					updateEntry(posA, rows[i][j], j);
				} else if (posB === 0) { // If undefined, that means it is an edge
					updatedPath = posA.path;
					updatedPath.push(parseInt(rows[i][j]));
					addEntry(posA.sum + parseInt(rows[i][j]), updatedPath);
				}
			}
		}

		// Determine which sum is greatest
		var maxSum   = 0;
		var bestPath = [];
		for (var k = 0; k < paths.length; k++) {
			if (paths[k].sum > maxSum) {
				maxSum   = paths[k].sum;
				bestPath = paths[k].path;
			}
		}

		//console.log(paths);
		//console.log("\nThe best path is:\n"+bestPath+"\n");
		return maxSum;
	}

	
	if (require.main === module) {
		var triangle = ''+
'75\n'+
'95 64\n'+
'17 47 82\n'+
'18 35 87 10\n'+
'20 04 82 47 65\n'+
'19 01 23 75 03 34\n'+
'88 02 77 73 07 63 67\n'+
'99 65 04 28 06 16 70 92\n'+
'41 41 26 56 83 40 80 70 33\n'+
'41 48 72 33 47 32 37 16 94 29\n'+
'53 71 44 65 25 43 91 52 97 51 14\n'+
'70 11 33 28 77 73 17 78 39 68 17 57\n'+
'91 71 52 38 17 14 91 43 58 50 27 29 48\n'+
'63 66 04 68 89 53 67 30 73 16 69 87 40 31\n'+
'04 62 98 27 23 09 70 98 73 93 38 53 60 04 23';

		console.log("The max sum is: "+maxPathSumI(triangle));
	}
})();

