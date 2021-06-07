 public static function duplicate_encode($word){
        // ...
        $lower = strtolower($word);
        $split = str_split($lower);
        $result = '';
        foreach ($split as $item){
            $checkDuplicate = array_count_values($split)[$item];
            if ($checkDuplicate > 1){
                $result .= ')';
            }else{
                $result .= '(';
            }
        }
        return $result;
    }
