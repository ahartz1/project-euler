var test = require('mocha').it,
    expect = require('chai').expect,
    assert = require('chai').assert,
    main = require('../e013large_sum.js');

const TEST_NUMS = `
123456789012
000000000000`;

test('largeSum', function() {
  expect(main.largeSum).is.a('function');
  // expect(main.largeSum(TEST_NUMS).is.a('number'));
  expect(main.largeSum(TEST_NUMS)).is.deep.equal(1234567890);
});
