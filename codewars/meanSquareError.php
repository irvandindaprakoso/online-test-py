function solution(array $a, array $b): float {
  // Your code here
  $result = 0;
  for ($i=0; $i<count($a); $i++){
    $result += pow($a[$i] - $b[$i],2);
  }
  return $result/count($a);
}
