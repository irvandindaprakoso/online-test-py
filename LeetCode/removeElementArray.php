function removeElement(&$nums, $val) {
        foreach($nums as $key => $num){
        
            if ($num == $val){
                unset($nums[$key]);
            }
        }
        return count($nums);
    }
