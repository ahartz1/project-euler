<?php
// Tests for Euler #17 Number Letter Counts


class NumberLetterCountsTest extends PHPUnit_Framework_TestCase
{

    /**
     * @param int $n Number up to which we want letter counts
     * @param int $expectedSum What letter count we expect
     *
     * @dataProvider providerTestNumberLetterCounts
     */
    public function testNumberLetterCounts($n, $expectedSum)
    {
        $euler = new Euler\E017NumberLetterCounts();

        $result = $euler->numberLetterCounts($n);

        $this->assertEquals($result, $expectedSum);
    }

    public function providerTestNumberLetterCounts()
    {
        return array(
            array(1,   3),
            array(5,   19),
            array(20,  112),
            array(21,  121),
            array(101, 870)
        );
    }
}

