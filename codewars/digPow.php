function digPow($n, $p) {
    // your code
  $result = 0;
  $splitN = array_map('intval', str_split($n));
  foreach ($splitN as $value){
    $result += pow($value, $p);
    $p++;
  }
  
  if ($result % $n != 0){
    return -1;
  }
  
  return $result / $n;
}
