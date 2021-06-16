public static function findParity($integers) {

        $even = [];
        $odd = [];

        $result = 0;

        foreach($integers AS $integer){
            $result = $integer % 2;

            if ($result != 0){
                $odd[] = $integer;
            }else{
                $even[] = $integer;
            }
        }

        if (count($even) == 1){
            $result = $even[0];
        }else{
            $result = $odd[0];
        }

        return $result;
    }
