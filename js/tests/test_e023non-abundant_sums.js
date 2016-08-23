/**
 * Tests for Project Euler #23: Non-Abundant Sums
 */

// Set up test environment
var test   = require('mocha').it;
var expect = require('chai').expect;
var assert = require('chai').assert;
var main   = require('../e023non-abundant_sums.js');

test('properDivisorSum', function() {
	expect(main.properDivisorSum).is.a('function');
	expect(main.properDivisorSum(10)).is.deep.equal(8);
	expect(main.properDivisorSum(12)).is.deep.equal(16);
	expect(main.properDivisorSum(16)).is.deep.equal(15);
});

test('nonAbundantSums', function() {
	expect(main.nonAbundantSums).is.a('function');
	expect(main.nonAbundantSums(5)).is.deep.equal(15);
	expect(main.nonAbundantSums(13)).is.deep.equal(91);
});

