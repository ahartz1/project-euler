<?php
// Tests for Euler #16 Power Digit Sum


class PowerDigitSumTest extends PHPUnit_Framework_TestCase
{
    /**
     * @param int $n The power of 2 of which to sum digits
     * @param int $expectedSum The expected sum of digits
     *
     * @dataProvider providerTestPowerDigitSum
     */
    public function testPowerDigitSum($n, $expectedSum)
    {
        // Arrange
        $euler = new Euler\E016PowerDigitSum();

        // Act
        $sum = $euler->powerDigitSum($n);

        // Assert
        $this->assertEquals($sum, $expectedSum);
    }

    public function providerTestPowerDigitSum()
    {
        return array(
            array(4,  7),
            array(15, 26)
        );
    }
}

