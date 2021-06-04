public static function reverseWords($str) {
        // Go for it
        $split = explode(' ', $str);

        $result = '';

        foreach ($split as $word){
            $reverse = strrev($word);
            $result .= ' ' .  $reverse;
        }

        return trim($result);

//        return implode(' ', array_reverse(explode(' ', strrev($str)))) ;

}
