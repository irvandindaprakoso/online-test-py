function generateHashtag($str) {
  $str = trim($str);
  $result = join("",array_map('ucfirst',explode(' ',$str)));

  if (strlen($result) > 139){
      return false;
  }
  
  if ($result != ''){
      return '#'.$result;
  }

  return false;
}
