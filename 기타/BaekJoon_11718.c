#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//BaekJoon_11718
int main(void)
{
	char result[100][100];
	int i = 0, j = 1;
	int str1 = 0;
	while (j <= 100)
	{
		gets(result[i]);


		str1 = strlen(result[i]);

		if (str1 > 100) {
			break;
		}
		i++;
		j++;
	}

	for (j = 0; j < i; j++)
		printf("%s\n", result[j]);

	return 0;
}