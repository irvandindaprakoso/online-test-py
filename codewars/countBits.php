function countBits(int $n): int {
   return strlen(str_replace('0', '', decbin($n)));
}
