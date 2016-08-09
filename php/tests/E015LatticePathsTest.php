<?php
// Tests for Project Euler #15 Lattice Paths


class NumLatticePathsTest extends PHPUnit_Framework_TestCase
{
    /**
     * @param int $gWidth Width of grid
     * @param int $gHeight Height of grid
     * @param int $expectedNumPaths Expected number of resulting lattice paths
     *
     * @dataProvider providerTestE015LatticePaths
     */
    public function testE015LatticePaths($gWidth, $gHeight, $expectedNumPaths)
    {
        // Arrange
        $euler = new Euler\E015LatticePaths();

        // Act
        $result = $euler->numLatticePaths($gWidth, $gHeight);

        // Assert
        $this->assertEquals($result, $expectedNumPaths);
    }

    public function providerTestE015LatticePaths()
    {
        return array(
            array(2, 2, 6),
            array(3, 3, 20),
            array(2, 3, 10)
        );
    }
}

