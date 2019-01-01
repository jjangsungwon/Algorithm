#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(void)
{
	int num1, temp,i,j=0,k;
	char ch[1000][30];
	int num2[1000] = { 0, };
	int len[1000] = { 0, };
	int count = 0;
	//input
	scanf("%d", &num1);
	
	//error check
	if (num1 < 1 || num1>1000)
		return 0;

	for (i = 0; i < num1; i++) {
		scanf("%d %s", &num2[i], ch[i]);
		len[i] = strlen(ch[i]);
		if (len[i] > 20)
			return 0;
		if (len[i] < 1)
			return 0;
	}

	for(i=0;i<num1;i++)
		len[i] = num2[i] * len[i];

	for (i = 0; i < num1; i++) 
	{
		for (k = 0; k < len[i]; k++) 
		{
			count++;
			printf("%c", ch[i][j]);
			if (count % num2[i] == 0)
				j++;
		}
		if (i == num1 - 1)
			break;
		puts("");
		j = 0;
		count = 0;
	}

	return 0;
}