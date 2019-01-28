#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

//JJangSungWon_1316
int main(void)
{
	int N;
	int i,j,k,len,temp=0,temp1=0;
	char str[101];
	char check[101][101];
	int total[100],count=0;
	int flag = 1;
	scanf("%d", &N); //총 케이스 개수

	for (i = 0; i < N; i++)
	{
		scanf("%s", str);

		len = strlen(str);

		for (j = 0; j < len; j++)
		{
			if(str[j + 1] != str[j])
				check[i][temp++] = str[j];
		}
		check[i][temp] = '\0';
		
		len = strlen(check[i]);
		total[temp1++] = len;
		temp = 0;
	}

	j = 0;

	for (i = 0; i < N; i++)
	{
		for (j = 0;j<total[i] ; j++)
		{
			if (flag == 0)
				break;
			for (k = j+1; k<total[i]; k++)
			{
				if (check[i][j] == check[i][k])
				{
					flag = 0;
					break;
				}
				else
					continue;
			}
		}
		if (flag == 0)
			flag = 1;
		else
		{
			count++;
		}
	}

	printf("%d", count);

	system("pause");
	return 0;
}