var test = require('mocha').it,
    expect = require('chai').expect,
    assert = require('chai').assert,
    main = require('./e14longest_collatz_sequence.js');

test('collatzSequenceLength', function() {
  expect(main.collatzSequenceLength).is.a('function');
  expect(main.collatzSequenceLength(13)).is.deep.equal(10);
});

test('longestCollatzSequence', function() {
  expect(main.longestCollatzSequence).is.a('function');
  expect(main.longestCollatzSequence(13)).is.deep.equal(9);
});
