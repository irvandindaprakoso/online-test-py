import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int sum=0;
        int n = in.nextInt();
        for(int i=0; i < n; i++){
            sum+= in.nextInt();
        }
        System.out.print(sum);
    }
}

