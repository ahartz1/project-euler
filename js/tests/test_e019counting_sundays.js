/**
 * Tests for Project Euler #19: Counting Sundays
 */

// Set up our test environment
var test   = require('mocha').it;
var expect = require('chai').expect;
var assert = require('chai').assert;
var main   = require('../e019counting_sundays.js');

test('countingSundays', function() {
	// Set up our test dates. (In JavaScript, months are zero-based.)
	var startDate1 = new Date(2017, 0, 1);
	var endDate1   = new Date(2017, 9, 31);
	var endDate2   = new Date(2018, 3, 30);
	
	expect(main.countingSundays).is.a('function');
	expect(main.countingSundays(startDate1, endDate1)).is.deep.equal(2);
	expect(main.countingSundays(startDate1, endDate2)).is.deep.equal(3);
});

