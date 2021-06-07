public static function isIsogram($string){
        // ...
        $arr = str_split(strtolower($string));
        $result = array_diff_assoc($arr, array_unique($arr));

        return $result == [];
}
