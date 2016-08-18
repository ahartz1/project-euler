/**
 * Project Euler Problem #19: Counting Sundays
 *
 * Given two dates (after 1/1/1900), determine how many Sundays fall on the
 * first of the month between them.
 *
 * Provided facts:
 * (1) 1/1/1900 was a Monday
 * (2) Months with 30 days: April, June, September, November
 *     Months with 31 days: January, March, May, July, August, October, December
 *     February has 28 days unless it is a leap year.
 * (3) Leap years: Any year divisible by 4, but not on a century unless divisible by 400
 */

;(function(){
	exports.countingSundays = countingSundays;

	/**
	 * How many days are in each month for the specified year?
	 *
	 * @param {number} year The year for which month durations are needed
	 *
	 * @return {Array.<number>} The month durations, zero-indexed
	 */
	function getMonthDurations(year) {
		var febDuration = 28;
		if (year % 4 === 0) {
			if (year % 100 === 0 && year % 400 !== 0) {
				// This is a non–leap year century
			} else {
				// This is a leap year
				febDuration = 29;
			}
		}
		return [31, febDuration, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
	}

	/**
	 * Calculate the sum of a and b.
	 *
	 * @param {number} a
	 * @param {number} b
	 *
	 * @return {number} The resulting sum
	 */
	function add(a, b) {
		return a + b;
	}

	/**
	 * How many months start with Sunday in the given interval?
	 *
	 * @param {Date} startDate A date object representing the start date
	 * @param {Date} endDate   A date object representing the end date
	 *
	 * @return {number} The number of months beginning on a Sunday between
	 *     startDate and endDate
	 */
	function countingSundays(startDate, endDate) {
		var numSundays     = 0;
		var totalDays      = 0;
		var monthDurations = 0;
		for (var i = 1900; i <= endDate.getFullYear(); i++) {
			if (i < startDate.getFullYear()) {
				// Count the days between 1900 and the current year
				totalDays += getMonthDurations(i).reduce(add, 0);
				continue;
			}
			monthDurations = getMonthDurations(i);
			for (var j = 0; j < monthDurations.length; j++) {
				if ((i === startDate.getFullYear() && j < startDate.getMonth()) ||
					(i === endDate.getFullYear() && j > endDate.getMonth())) {
					// If not yet to start date, just add the days
					totalDays += monthDurations[j];
					continue;
				}
				if (totalDays % 7 === 6) {
					numSundays++;
				}
				totalDays += monthDurations[j];
			}
		}
		return numSundays;
	}

	
	if (require.main === module) {
		var startDate = new Date(1901, 0, 1);
		var endDate   = new Date(2000, 11, 31);
		console.log('The number of Sundays falling on the first of the month between\n\t'+
				startDate.toDateString()+'\n\t      and\n\t'+
				endDate.toDateString()+'\n>>> '+countingSundays(startDate, endDate));
	}
})();

