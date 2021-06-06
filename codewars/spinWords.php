function spinWords(string $str): string {
  // TODO Have fun :)
  $split = explode(' ', $str);
  foreach ($split as $item){
    if (strlen($item) >= 5){
      $str = str_replace($item,strrev($item), $str);
    }
  }
  
  return $str;
}
