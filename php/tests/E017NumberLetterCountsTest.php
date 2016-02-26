<?php
// Tests for Euler #17 Number Letter Counts


class NumberLetterCountsTest extends PHPUnit_Framework_TestCase
{
    protected $p;

    protected function setUp() {
        $this->p = new Euler\E017NumberLetterCounts();
    }

    public function testUpTo1() {
        // Arrange (taken care of in setUp)

        // Act
        $sum = $this->p->numberLetterCounts(1);

        // Assert
        $this->assertEquals(3, $sum);
    }

    public function testUpTo5() {
        // Arrange (taken care of in setUp)

        // Act
        $sum = $this->p->numberLetterCounts(5);

        // Assert
        $this->assertEquals(19, $sum);
    }

    public function testUpTo20() {
        // Arrange (taken care of in setUp)

        // Act
        $sum = $this->p->numberLetterCounts(20);

        // Assert
        $this->assertEquals(112, $sum);
    }

    public function testUpTo21() {
        // Arrange (taken care of in setUp)

        // Act
        $sum = $this->p->numberLetterCounts(21);

        // Assert
        $this->assertEquals(115, $sum);
    }
}

