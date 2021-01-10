import java.util.*;
import java.io.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        
        int[] people = new int[n];
        
        for(int i=0; i<n; i++){
            people[i] = 1; // 모두 체육복이 있다고 가정합니다.
        }
        
        // 여벌 체육복이 있는 학생의 정보를 업데이트합니다.
        for(int i=0; i<reserve.length; i++){
            people[reserve[i] - 1] = 2;
        }
        
        // 체육복을 도난당한 학생의 정보를 업데이트합니다.
        for(int i=0; i<lost.length; i++){
            people[lost[i] - 1] -= 1;
        }
        
        
        // 1번 학생부터 탐색합니다.
        for(int i=0; i<n; i++){
            if(people[i] >= 1){ // 체육복이 1개 이상 있으면 넘어갑니다.
                answer += 1;
            }
            else if(people[i] == 0){
                if(i != n - 1 && people[i + 1] == 2){ // 뒷번호 친구에게 체육복을 빌립니다.
                    answer += 1;
                    people[i + 1] -= 1;
                }
                else if(i != 0 && people[i - 1] == 2){ // 앞번호 친구에게 체육복을 빌립니다.
                    answer += 1;
                    people[i - 1] -= 1;
                }
            }
        }
        
        return answer;
    }
}