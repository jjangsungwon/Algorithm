package practice;

class Solution {
    public String solution(String s, int n) {
        String answer = "";
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) == ' '){
                answer += " ";
            }else if('a' <= s.charAt(i)){
                int temp = (s.charAt(i) - 97 + n) % 26 + 97;
                answer += (char) temp;
            }else{
                int temp = (s.charAt(i) - 65 + n) % 26 + 65;
                answer += (char) temp;
            }
        }
        return answer;
    }
}
