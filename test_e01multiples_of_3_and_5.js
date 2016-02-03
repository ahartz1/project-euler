var test = require('mocha').it,
    expect = require('chai').expect,
    assert = require('chai').assert,
    main = require('./e01multiples_of_3_and_5.js');

test('sumOf3sAnd5s', function(){
  expect(main.sumOf3sAnd5s).is.a('function');
  expect(main.sumOf3sAnd5s(3)).is.an('number');
  expect(main.sumOf3sAnd5s(3)).is.deep.equal(3);
  assert.deepEqual(main.sumOf3sAnd5s(3), 3);
  assert.deepEqual(main.sumOf3sAnd5s(6), 14);
});
