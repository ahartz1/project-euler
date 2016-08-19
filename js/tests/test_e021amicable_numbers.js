/**
 * Tests for Project Euler #21: Amicable Numbers
 */

// Set up test environment
var test   = require('mocha').it;
var expect = require('chai').expect;
var assert = require('chai').assert;
var main   = require('../e021amicable_numbers.js');

test('divisorSum', function() {
	expect(main.divisorSum).is.a('function');
	expect(main.divisorSum(10)).is.deep.equal(8);
	expect(main.divisorSum(12)).is.deep.equal(16);
	expect(main.divisorSum(16)).is.deep.equal(15);
});

test('isAmicable', function() {
	expect(main.isAmicable).is.a('function');
	expect(main.isAmicable(220)).is.deep.equal(284);
});

test('amicableNumberSum', function() {
	expect(main.amicableNumberSum).is.a('function');
	expect(main.amicableNumberSum(285)).is.deep.equal(504);
});

