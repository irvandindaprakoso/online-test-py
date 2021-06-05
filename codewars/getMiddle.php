public static function getMiddle($text)
{
	if (strlen($text) % 2 == 0){
            return substr($text,strlen($text)/2 -1, 2);
        }
        return substr($text,(int)round(strlen($text)/2 -1), 1);
 }
