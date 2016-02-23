<?php
// Project Euler #16 Power Digit Sum
//
// The goal is to sum the digits in the result of 2^n. With large values of n,
// the limits of regular ints are exceeded, so bcpow is used here to achieve
// arbitrary precision.


class e16Power_Digit_Sum
{
    public function powerDigitSum($n) {
        $pow = bcpow(2, $n);
        $powString = strval($pow);
        $ret = 0;
        for ($i = 0; $i < strlen($powString); $i++) {
            $ret += intval($powString[$i]);
        }
        return $ret;
    }
}

if (!count(debug_backtrace())) {
    $eulerNum = 1000;
    $eulerPow = pow(2, $eulerNum);
    $p = new e16Power_Digit_Sum();
    echo "2^{$eulerNum} = {$eulerPow}\n";
    echo "Sum of digits = {$p->powerDigitSum($eulerNum)}\n";
}

