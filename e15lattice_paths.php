<?php
// Project Euler #15 Lattice Paths
// Find the number of paths from the top left to the bottom right of a grid
// of dimension width x height.

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

echo "This will take a long time..., eventually it will answer: 137846528820";
$eulerWidth = 20;
$eulerHeight = 20;
echo "Number of lattice paths in " . $eulerWidth . "x" . $eulerHeight
    . " grid: " . numLatticePaths($eulerWidth, $eulerHeight);

