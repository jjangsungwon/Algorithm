#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
/*
	baekjoon_1712
	github : JJANGSUNGWON
	A : 고정 비용, B : 가변 비용, C : 노트북 가격
	총 수입(판매비용)이 총 비용(고정비용 + 가변비용)보다 많아지는 지점을 출력.
	
	1. 가변 비용과 노트북 가격의 차이를 구한다.
	2. 고정 비용 / 차이를 이용해서 결과를 구한다.
*/

int main(void)
{
	int A, B, C;
	int difference;
	int count = 0;
	scanf("%d %d %d", &A, &B, &C);

	difference = C - B;

	if (difference > A)
		printf("%d", 1);
	else if (B == C)
		printf("%d", -1);
	else {
		if (!A % difference)
			count = A / difference;
		else
			count = A / difference + 1;

		if (count < 0)
			printf("%d", -1);
		else
			printf("%d", count);
	}

	return 0;
}