/**
 * Tests for Project Euler #22: Names Scores
 */

// Set up test environment
var test   = require('mocha').it;
var expect = require('chai').expect;
var assert = require('chai').assert;
var main   = require('../e022names_scores.js');

test('alphabeticalSum', function() {
	expect(main.alphabeticalSum).is.a('function');
	expect(main.alphabeticalSum('mary')).is.deep.equal(57);
	expect(main.alphabeticalSum('patricia')).is.deep.equal(77);
});

test('namesScoresSum', function() {
	expect(main.namesScoresSum).is.a('function');
	expect(main.namesScoresSum('data/test_names1.txt')).is.deep.equal(57);  // "MARY"
	expect(main.namesScoresSum('data/test_names2.txt')).is.deep.equal(211); // "PATRICIA","MARY"
});

