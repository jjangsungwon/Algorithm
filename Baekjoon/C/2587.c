#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJangSungWon BaekJoon_2587
int main(void)
{
	int sum = 0, i,j,mid;
	int num[5],temp;

	for (i = 0; i < 5; i++) {
		scanf("%d", &num[i]);

		if (num[i] > 100)
			return 0;

		sum += num[i];
	}

	for (i = 0; i < 5; i++)
	{
		for (j = 0; j < 5; j++)
		{
			if (num[i] > num[j])
			{
				temp = num[i];
				num[i] = num[j];
				num[j] = temp;
			}
		}
	}

	for (i = 0; i < 5; i++)
		if (i == 2)
			mid = num[i];

	printf("%d\n", sum/5);
	printf("%d", mid);
	
	system("pause");
	return 0;
}