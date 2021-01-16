package practice;

class Solution {
    public int solution(String s) {
        int answer = 0;
        char first_char = s.charAt(0);
        if(first_char == '-' || first_char == '+'){ // 음수
            for(int i=1; i<s.length(); i++){
                int num = s.charAt(i) - '0';
                answer += Math.pow(10, s.length() - i - 1) * num;
            }
            if(first_char == '-'){
                answer *= -1;
            }
        }else{ // 양수
            for(int i=0; i<s.length(); i++){
                int num = s.charAt(i) - '0';
                answer += Math.pow(10, s.length() - i - 1) * num;
            }
        }
        return answer;
    }
}
