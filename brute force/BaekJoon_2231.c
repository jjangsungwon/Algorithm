#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
/*
	baekjoon_2231
	github : JJANGSUNGWON
	분해합. 가장 작은 생성자를 찾기.
	ex) 245 -> 245 + 2 + 4 + 5 = 256 (256의 생성자는 245)
	대단한 알고리즘이 있는줄 알았는데 
	256을 입력했으면 255부터 하나씩 내려가면서 다해보고 245를 찾고 쭉쭉 내려간다.
*/

int main(void)
{
	int N;
	int M, ans = 0;

	//input
	scanf("%d", &N);

	M = N;

	while (--M > 1)
	{
		int tmp = M;
		int sum = tmp;

		do {
			sum += tmp % 10;
			tmp /= 10;
		} while (tmp > 0);

		if (N == sum)
			ans = M;
	}

	printf("%d", ans);
	
	return 0;
}