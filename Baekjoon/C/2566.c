#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJangSungWon BaekJoon_2566
int main(void)
{
	int i, j,flag=1,max;
	int x, y;
	int num;

	for (i = 1; i <= 9; i++)
	{
		for (j = 1; j <= 9; j++)
		{
			scanf("%d", &num);

			if (num >= 100)
				return 0;
			if (flag)	
			{
				max = num;
				x = i;
				y = j;
				flag = 0;
			}
			else
			{
				if (max < num) {
					max = num;
					x = i;
					y = j;
				}
			}
		}
	}

	printf("%d\n", max);
	printf("%d %d", x, y);
	//system("pause");
	return 0;
}