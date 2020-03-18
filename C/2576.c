#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJangSungWon BaekJoon_2576
int main(void)
{
	int i, sum = 0, min;
	int num, flag=1;
	int count = 0;
	for (i = 0; i < 7; i++)
	{
		scanf("%d", &num);

		if (num > 100 || num < 1)
			return 0;
		if (num % 2) //È¦¼ö
		{
			count++;
			if (flag) { //Ã³À½
				min = num;
				flag = 0;
				sum += num;
			}
			else {
				sum += num;
				if (min > num)
					min = num;
			}
		}
	}

	if (count == 0)
		printf("-1");
	else {
		printf("%d\n", sum);
		printf("%d", min);
	}
	//system("pause");
	return 0;
}