class Solution {
    public boolean solution(String s) {
        if(s.length() != 4 && s.length() != 6){  // 문자열 s의 길이가 4 혹은 6이 아닌 경우
            return false;
        }else{
            for(int i=0; i<s.length(); i++){
                if('0' > s.charAt(i) || s.charAt(i) >'9'){
                    return false;
                }
            }
        }
        return true;
    }
}