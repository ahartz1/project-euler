<?php
// Tests for Project Euler #15 Lattice Paths

class TestNumLatticePaths extends PHPUnit_Framework_TestCase
{
    public function testKnownGrid2x2()
    {
        $this->assertEquals(numLatticePaths(2, 2), 6);
    }

    public function testKnownGrid3x3()
    {
        $this->assertEquals(numLatticePaths(3, 3), 20);
    }
}


function numLatticePaths($width, $height)
{
     // Recursive definition is going to work well here. If we have a
     // column or row of dimension 1, the number of paths is the number of
     // edges in the other dimension.

     // Base case 1
     if ($width === 1) {
         return $height + 1;
     }

     // Base case 2
     if ($height === 1) {
         return $width + 1;
     }

     // Recursive case: reduce by one column and sum resulting grids
     $reducedWidth = $width - 1;
     $ret = 1;
     for ($i = 0; $i < $height; $i++) {
         $ret += numLatticePaths($reducedWidth, $height - $i);
     }

     return $ret;
}

