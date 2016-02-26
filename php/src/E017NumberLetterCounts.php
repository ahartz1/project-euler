<?php
/**
 * Project Euler #17 Number Letter Counts
 *
 * Sum the number of letters used to write each number between 1 and n in
 * English. (e.g., 342 [three hundred and forty-two] contains 23 letters)
 * Spaces and hyphens do not count.
 */

namespace Euler;

class E017NumberLetterCounts
{
    public function numberLetterCounts($n) {
        /**
         * First, build the arrays that have the corresponding letter counts
         *
         * $onesTens starts at 'one' and goes through 'nineteen', by 1s
         * (position in array is value - 1)
         *
         * $tenNinety starts at 'ten' and goes through 'ninety', by 10s
         * (position in array is value - 1)
         */

        $ones = array(3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8);
        $tenNinety = array(3, 6, 6, 5, 5, 5, 7, 6, 5);

        $ret = 0;

        for ($i = 1; $i <= $n; $i++) {

            // Between 1 and 19, use value from $ones using $i directly
            if (1 <= $i && $i <= 19) {
                $ret += $ones[$i -1];
                continue;
            }
  
            // Prep for calculations
            $loopRet = 0;
            $iAsRevString = strrev(strval($i));

            // Look through reversed string value of $i
            for ($j = 0; $j < strlen($iAsRevString); $j++) {

                // If 0 in ones place, nothing needed from $ones (<20 handled above)
                if ($j === 0 && $iAsRevString[$j] == 0) {
                    $ret += $tenNinety[$iAsRevString[$j + 1] - 1];
                    $j++;
                    continue;
                }
            }
            $ret += $loopRet;
        }
        return $ret;
    }
}

if (! count(debug_backtrace())) {
    $eulerNum = 20;  // 1000
    $p = new E017NumberLetterCounts();
    echo "Sum of letters of the written numbers from 1 to {$eulerNum}" .
       " = {$p->numberLetterCounts($eulerNum)}\n";
}

