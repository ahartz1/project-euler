var test = require('mocha').it,
    expect = require('chai').expect,
    assert = require('chai').assert,
    main = require('../e12highly_divisible_triangular_number.js');

test('triangularDivisors', function() {
  expect(main.triangularDivisors).is.a('function');
  expect(main.triangularDivisors(2)).is.a('number');
  expect(main.triangularDivisors(2)).is.deep.equal(6);
  expect(main.triangularDivisors(4)).is.deep.equal(28);
  expect(main.triangularDivisors(5)).is.deep.equal(28);
  assert.deepEqual(main.triangularDivisors(2), 6);
  assert.deepEqual(main.triangularDivisors(4), 28);
});
