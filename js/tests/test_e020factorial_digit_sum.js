/**
 * Tests for Project Euler #20: Factorial Digit Sum
 */

// Set up test environment
var test   = require('mocha').it;
var expect = require('chai').expect;
var assert = require('chai').assert;
var main   = require('../e020factorial_digit_sum.js');

test('factorialDigitSum', function() {
	expect(main.factorialDigitSum).is.a('function');
	expect(main.factorialDigitSum(5)).is.deep.equal(3);
	expect(main.factorialDigitSum(10)).is.deep.equal(27);
});

