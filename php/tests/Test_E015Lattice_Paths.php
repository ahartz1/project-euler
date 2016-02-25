<?php
// Tests for Project Euler #15 Lattice Paths

// require_once(realpath(dirname(__FILE__)) . "/../src/E015LatticePaths.php");

class TestNumLatticePaths extends PHPUnit_Framework_TestCase
{
    protected $euler;

    protected function setUp() {
        $this->euler = new Euler\E015Lattice_Paths();
    }

    public function testKnownGrid2x2()
    {
        $this->assertEquals($this->euler->numLatticePaths(2, 2), 6);
    }

    public function testKnownGrid3x3()
    {
        $this->assertEquals($this->euler->numLatticePaths(3, 3), 20);
    }

    public function testKnownGrid2x3()
    {
        $this->assertEquals($this->euler->numLatticePaths(2, 3), 10);
    }
}

