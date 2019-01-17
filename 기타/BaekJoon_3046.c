#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJangSungWon BaekJoon_3046
int main(void)
{
	int R1, R2, S;

	scanf("%d %d", &R1, &S);

	if (R1 < -1000 || S < -1000)
		return 0;

	if (R1 > 1000 || S > 1000)
		return 0;

	R2 = S * 2 - R1;

	printf("%d", R2);

	//system("pause");
	return 0;
}