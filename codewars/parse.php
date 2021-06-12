public static function parse($data)
    {
        $result = [];

        $split = str_split($data);

        $temp = 0;

        foreach ($split as $item) {
            if ($item === 's') {
                $temp = $temp ** 2;
            }
            if ($item === 'i') {
                $temp += 1;
            }
            if ($item === 'd') {
                $temp += -1;
            }
            if ($item === 'o') {
                $result[] = $temp;
            }
        }

        return $result;
    }
