class Solution {
    public int tribonacci(int n) {
        // int t0=0;
        // int t1=1,t2=1;
        // int prevSum=t0+t1+t2;
        int sum=0;
        int maxNumber = n; 
		int t0 = 0;
		int t1 = 1;
        int t2 = t0+t1;
        int t3 = t0+t1+t2;
        if (n<=3){
            if (n==0){
                return t0;
            }
            else if(n==1){
                return t1;
            }
            else if(n==2){
                return t2;
            }
            else{
                return t3;
            }
        }
        for (int i = 4; i <= maxNumber; ++i)
        {
            sum = t1 + t2 + t3;
            t1 = t2;
            t2 = t3;
            t3 = sum;
        }
        return sum;
    }
}
