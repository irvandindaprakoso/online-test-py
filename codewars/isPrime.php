public static function isPrime($n)
    {
        if ($n <= 1) {
            return false;
        }
        $x = floor(sqrt($n));

        for ($i = 2; $i <= $x; $i ++) {

            if ($n % $i == 0) {
                return false;
            }
        }

        return true;
    }
