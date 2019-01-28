#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

//JJangSungWon_11721
int main(void)
{
	char str[200];
	int len,i;

	scanf("%s", str);

	len = strlen(str);

	for (i = 1; i <= len; i++)
	{
		printf("%c", str[i-1]);
		if (!(i % 10))
			puts("");
	}

	system("pause");
	return 0;
}