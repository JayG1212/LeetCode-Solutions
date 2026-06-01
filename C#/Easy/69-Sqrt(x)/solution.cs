public class Solution {
    public int MySqrt(int x) {
        long product = 0;
        for(long i = 0; i <= x; i++){
            product = i * i;
            if(product == x){
                return (int)i;
            }
            else if(product > x){
                return (int)i - 1;
            }
        }
        return x;
    }
}