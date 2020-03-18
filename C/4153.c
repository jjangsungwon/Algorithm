#define _CRT_SECURE_NO_WARNINGS

//BaekJoon_4153
#include<stdio.h>

int flag[10000] = { 0, };
int n[10000][3] = { 0, };

int main(void)
{
	int count = 0;
	int temp = 0;
	int num1, num2, num3;

	scanf("%d %d %d", &n[count][0], &n[count][1], &n[count][2]);

	if (n[count][0] != 0 && n[count][1] != 0 && n[count][2] != 0)
		count++;
	else
		return 0;

	//input
	while (1) {

		scanf("%d %d %d", &n[count][0], &n[count][1], &n[count][2]);

		//세 값이 0이 들어온다면
		if (n[count][0] == 0 && n[count][1] == 0 && n[count][2] == 0)
			break;

		count++;
	}

	//sort
	for (int i = 0; i < count; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			for (int k = j; k < 3; k++)
			{
				if (n[i][j] < n[i][k])
				{
					temp = n[i][j];
					n[i][j] = n[i][k];
					n[i][k] = temp;
				}
			}
		}
	}

	for (int i = 0; i < count; i++)
	{
		num1 = n[i][0] * n[i][0];
		num2 = n[i][1] * n[i][1];
		num3 = n[i][2] * n[i][2];
		
		if (i + 1 != count) 
		{
			if (num1 == (num2 + num3))
				printf("right\n");
			else
				printf("wrong\n");
		}
		else
		{
			if (num1 == (num2 + num3))
				printf("right");
			else
				printf("wrong");
		}
	}

	return 0;
}