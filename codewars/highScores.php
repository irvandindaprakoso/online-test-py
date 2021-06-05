public static function high($x) {
        $lower = strtolower($x);
        $split = explode(' ', $lower);

        $alphabet = range('a', 'z');

        $result = '';
        $max = 0;
        foreach ($split as $items){
            $temp = 0;

            for ($i = 0, $iMax = strlen($items); $i < $iMax; $i++){
                $temp += array_search($items[$i], $alphabet) + 1;
            }

            if ($temp > $max){
                $max = $temp;
                $result = $items;
            }
        }
        return $result;
 }
