<?php
// Tests for Euler #16 Power Digit Sum


class TestPowerDigitSum extends PHPUnit_Framework_TestCase
{
    protected $p;

    protected function setUp() {
        $this->p = new Euler\E016Power_Digit_Sum();
    }

    public function test2ToThe4() {
        // Arrange (taken care of in setUp)

        // Act
        $sum = $this->p->powerDigitSum(4);

        // Assert
        $this->assertEquals(7, $sum);
    }

    public function test2ToThe15() {
        // Arrange (taken care of in setUp)

        // Act
        $sum = $this->p->powerDigitSum(15);

        // Assert
        $this->assertEquals(26, $sum);
    }
}

