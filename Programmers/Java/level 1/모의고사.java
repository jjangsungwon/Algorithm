import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        int[] f = {1, 2, 3, 4, 5};
        int[] s = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] t = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int f_index = 0, s_index = 0, t_index = 0;
        int f_score = 0, s_score = 0, t_score = 0;
        
        for(int i=0; i<answers.length; i++){
            // 수포자 1
            if(answers[i] == f[f_index]){
                f_score += 1;
            }
            // 수포자 2
            if(answers[i] == s[s_index]){
                s_score += 1;
            }
            // 수포자 3
            if(answers[i] == t[t_index]){
                t_score += 1;
            }
            f_index += 1;
            s_index += 1;
            t_index += 1;
            if(f_index == f.length){
                f_index = 0;
            }
            if(s_index == s.length){
                s_index = 0;
            }
            if(t_index == t.length){
                t_index = 0;
            }
        }
        
        // 최대 점수 찾기
        int max_value = Math.max(Math.max(f_score, s_score), t_score);
        if(f_score == max_value){
            list.add(1);
        }
        if(s_score == max_value){
            list.add(2);
        }
        if(t_score == max_value){
            list.add(3);
        }
        
        int[] answer = new int[list.size()];
        for(int i=0; i<list.size(); i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}