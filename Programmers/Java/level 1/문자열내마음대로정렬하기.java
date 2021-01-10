import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];
        
        for(int i=0; i<strings.length; i++){
            strings[i] = strings[i].charAt(n) + strings[i];
        }
        Arrays.sort(strings);
        for(int i=0; i<strings.length; i++){
            answer[i] = strings[i].substring(1, strings[i].length());
        }
        
        return answer;
    }
}