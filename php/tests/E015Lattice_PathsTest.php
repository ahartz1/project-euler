<?php
// Tests for Project Euler #15 Lattice Paths


class NumLatticePathsTest extends PHPUnit_Framework_TestCase
{
    /**
     * @param int $gWidth Width of grid
     * @param int $gHeight Height of grid
     * @param int $expectedNumPaths Expected number of resulting lattice paths
     *
     * @dataProvider providerTestE015Lattice_Paths
     */
    public function testE015Lattice_Paths($gWidth, $gHeight, $expectedNumPaths)
    {
        $euler = new Euler\E015Lattice_Paths();

        $result = $euler->numLatticePaths($gWidth, $gHeight);

        $this->assertEquals($result, $expectedNumPaths);
    }

    public function providerTestE015Lattice_Paths()
    {
        return array(
            array(2, 2, 6),
            array(3, 3, 20),
            array(2, 3, 10)
        );
    }
}

