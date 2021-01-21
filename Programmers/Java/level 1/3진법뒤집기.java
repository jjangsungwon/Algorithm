class Solution {
    public int solution(int n) {
        String ten_to_ternary = ternary(n);
        int answer = 0;
        int val = 1;
        for(int i=ten_to_ternary.length()-1; i>=0; i--){
            char temp = ten_to_ternary.charAt(i);
            if(temp != '0'){
                answer += val * (temp - '0');
            }
            val *= 3;
        }
        return answer;
    }
    
    public String ternary(int n){
        String answer = "";
        while(n > 0){
            answer += n % 3;
            n /= 3;
        }
        return answer;
    }
}