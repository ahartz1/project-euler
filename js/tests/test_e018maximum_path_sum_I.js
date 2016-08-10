var test = require('mocha').it,
    expect = require('chai').expect,
    assert = require('chai').assert,
    main = require('../e018maximum_path_sum_I.js');

var mini = ""+
'3\n'+
'7 4';

var babySteps = mini + "\n" +
'2 4 6';

var smallTriangle = babySteps + "\n" +
'8 5 9 3';

test('maxPathSumI', function() {
  expect(main.maxPathSumI).is.a('function');
  expect(main.maxPathSumI(mini)).is.deep.equal(10);
  expect(main.maxPathSumI(babySteps)).is.deep.equal(14);
  expect(main.maxPathSumI(smallTriangle)).is.deep.equal(23);
});

