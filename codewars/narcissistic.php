function narcissistic(int $value): bool {
        // Your code here

        $split = array_map('intval', str_split($value));
        $result = 0;
        foreach ($split as $item){
            $result += $item ** count($split);
        }

        return $result == $value;
    }
