#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<math.h>
#include<stdlib.h>

//JJangSungWon BaekJoon_1075
int digit(int n);

int main(void)
{
	int N, F,copy,i;
	int num, sub, count=0;

	scanf("%d", &N);
	scanf("%d", &F);

	copy = N; //복사본

	sub = N % 10; //1의자리
	copy = copy - sub; //1의자리 0으로 만들기

	sub = copy % 100; //10의자리
	copy = copy - sub; //1의자리, 10의자리 0으로 만든 상태


	for (i = copy; ; i++) //0으로 만든 수 for문 진행
	{
		if (i%F == 0) //나눠떨어지면 종료
			break;
		else
			count++;
	}
	
	if (count < 10)
		printf("0%d", count);
	else
		printf("%d", count);
	
	return 0;
}