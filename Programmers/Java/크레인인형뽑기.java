import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0; // 사라진 인형의 개수
        Stack<Integer> s = new Stack<Integer>();
        // moves 길이만큼 반복을 진행합니다.
        
        for(int i=0; i<moves.length; i++){
            int target = 0;
            //System.out.println(s);
            //System.out.println(target);
            for(int j=0; j<board.length; j++){
                if(board[j][moves[i] - 1] != 0){ // 인형을 집을 수 있는 상황입니다.
                    target = board[j][moves[i] - 1];
                    board[j][moves[i] - 1] = 0;  // 빈칸으로 수정합니다.
                    break;
                }else{
                    continue;
                }
            }
            if(target == 0){ // 아무일도 하지 않습니다.
                continue;
            }else{
                if(s.empty()){
                    s.add(target);
                }else{
                    if(s.peek() == target){
                        s.pop();
                        answer += 2;
                    }else{
                        s.add(target);
                    }
                }
            }
        }
    
        return answer;
    }
}