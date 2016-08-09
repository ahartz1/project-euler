<?php
// Project Euler #15 Lattice Paths
// Find the number of paths from the top left to the bottom right of a grid
// of dimension width x height.

namespace Euler;

class E015Lattice_Paths
{
    public $pathHolder = array();

    public function numLatticePaths($width, $height)
    {
         // Recursive definition is going to work well here. If we have a
         // column or row of dimension 1, the number of paths is the number of
         // edges in the other dimension. Because the processing time is long,
         // whenever a result is calculated, it is placed into a map for later
         // reference.
    
         // Base case 1
         if ($width === 1) {
             return $height + 1;
         }
    
         // Base case 2
         if ($height === 1) {
             return $width + 1;
         }

         // Check to see if answer is already in class dictionary
         if (key_exists($width.'x'.$height, $this->pathHolder)) {
             return $this->pathHolder[$width.'x'.$height];
         } elseif (key_exists($height.'x'.$width, $this->pathHolder)) {
             return $this->pathHolder[$height.'x'.$width];
         }
    
         // Recursive case: reduce by one column and sum resulting grids
         $reducedWidth = $width - 1;
         $ret = 1;
         for ($i = 0; $i < $height; $i++) {
             $ret += $this->numLatticePaths($reducedWidth, $height - $i);
         }
    
         // Save result into dictionary for future calls
         $this->pathHolder[$width.'x'.$height] = $ret;
         return $ret;
    }
}

if (!count(debug_backtrace())) {
    $eulerWidth = 20;
    $eulerHeight = 20;
    $euler = new E015Lattice_Paths();
    echo "Number of lattice paths in " . $eulerWidth . "x" . $eulerHeight
        . " grid: " . $euler->numLatticePaths($eulerWidth, $eulerHeight) . "\n";
}

