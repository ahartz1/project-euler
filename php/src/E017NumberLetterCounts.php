<?php
/**
 * Project Euler #17 Number Letter Counts
 *
 * Sum the number of letters used to write each number between 1 and n in
 * English. (e.g., 342 [three hundred and forty-two] contains 23 letters)
 * Spaces and hyphens do not count. Supported up to 999,999,999,999,999, but
 * not optimized to return in reasonable time.
 */

namespace Euler;

class E017NumberLetterCounts
{
    private $ones = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8];
    private $tenNinety = [3, 6, 6, 5, 5, 5, 7, 6, 5];
    private $suffixes = [0, 8, 7, 7, 8];

    public function numberLetterCounts($n)
    {
        /**
         * Loop through all numbers 1-n, chunking each number into 3-digit
         * groups and sending each to singleNumberHundreds and summing the
         * results
         */

        $ret = 0;

        for ($i = 1; $i <= $n; $i++) {
            $iAsString = strval($i);

            $big = false;
            if (strlen($iAsString) > 2) {
                $big = true;
            }

            $count = 0;
            while ($iAsString) {
                $iGroup = intval(substr($iAsString, -3, 3));
                $ret += $this->singleNumberHundreds($iGroup, $big, $count);
                $iAsString = substr($iAsString, 0, max([0, strlen($iAsString) - 3]));
                $count++;
            }
        }
        return $ret;
    }

    public function singleNumberHundreds($n, $big, $suffix)
    {
        /**
         * This function is responsible for returning the count of any 3-digit
         * number letter total, with a given suffix degree. Suffix degree 0
         * adds nothing to each total, but adds 'and' between hundreds (if
         * present) and last two digits. Suffix degree 1 adds 'thousand', 2
         * adds 'million', etc.
         *
         * First, build the arrays that have the corresponding letter counts
         *
         * $onesTens starts at 'one' and goes through 'nineteen', by 1s
         * (position in array is value - 1)
         *
         * $tenNinety starts at 'ten' and goes through 'ninety', by 10s
         * (position in array is tens digit - 1)
         *
         * $suffixes represent something added to each number (e.g., 'billion')
         */

        $ones = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8];
        $tenNinety = [3, 6, 6, 5, 5, 5, 7, 6, 5];
        $suffixes = [0, 8, 7, 7, 8];

        if ($n === 0) {
            return 0;
        }

        // Check if $n is an even hundred
        if ($n % 100 === 0) {
            return $this->ones[($n / 100) - 1] + 7 + $this->suffixes[$suffix];
        }

        $ret = 0;
        $nAsRevString = strrev(strval($n));
        $nLen = strlen($nAsRevString);

        // Look through reversed string value of $n
        for ($j = 0; $j < $nLen; $j++) {

            if ($n % 100 <= 19 && $j === 0) {
                // Add 3 for 'and' if in _last_ 3-digit group
                if ($suffix === 0 && $big) {
                    $ret += 3;
                }
                $ret += $this->ones[($n % 100) - 1];
                $j++;
                continue;
            }

            // If 0 in ones place, nothing needed from $ones (<20 and 100s
            // handled above)
            if ($j === 0 && $nAsRevString[$j] == 0) {
                if ($suffix === 0 && $big) {
                    $ret += 3;
                }
                $ret += $this->tenNinety[$nAsRevString[$j + 1] - 1];
                $j++;
                continue;
            }

            $jNum = intval($nAsRevString[$j]);

            switch ($j): 
                case 0:
                    $ret += $this->ones[$jNum - 1];
                    continue;
                case 1:
                    if ($suffix === 0 && $big) {
                        $ret += 3;
                    }
                    $ret += $this->tenNinety[$jNum - 1];
                    continue;
                case 2:
                    $ret += $this->ones[$jNum - 1] + 7;
            endswitch;
        }
        return $ret + $this->suffixes[$suffix];
    }
}

if (! count(debug_backtrace())) {
    $eulerNum = 1000;  // 1000
    $p = new E017NumberLetterCounts();
    echo "Sum of letters of the written numbers from 1 to {$eulerNum}" .
             " = {$p->numberLetterCounts($eulerNum)}\n";
}

