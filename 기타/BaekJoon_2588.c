#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJangSungWon BaekJoon_2588
int main(void)
{
	int n1, n2;
	int result[3];
	int sum=0;
	int num2[3];
	int div = 100;
	int copy;

	scanf("%d", &n1);
	scanf("%d", &n2);

	copy = n2;
	//n2의 자리 수 배열에 넣기
	for (int i = 2; i >=0; i--)
	{
		num2[i] = copy / div;
		copy = copy % div;
		div = div / 10;
	}

	for(int i=0;i<3;i++)
		result[i] = n1 * num2[i];

	div = 1;
	for (int i = 0; i < 3; i++) {
		sum += result[i] * div;
		div = div * 10;
	}

	for (int i = 0; i < 3; i++)
		printf("%d\n", result[i]);
	
	printf("%d\n", sum);
	//system("pause");
	return 0;
}