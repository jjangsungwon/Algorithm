#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

char electric[100][100];
int save[1000001];

//JJangSungWon BaekJoon_1076
int main() {

	char value1[30], value2[30], mul[30];
	unsigned long long int result,i;

	strcpy(electric[0], "black");
	strcpy(electric[1], "brown");
	strcpy(electric[2], "red");
	strcpy(electric[3], "orange");
	strcpy(electric[4], "yellow");
	strcpy(electric[5], "green");
	strcpy(electric[6], "blue");
	strcpy(electric[7], "violet");
	strcpy(electric[8], "grey");
	strcpy(electric[9], "white");

	scanf("%s", value1);
	scanf("%s", value2);
	scanf("%s", mul);

	for (i = 0; i < 10; i++)
	{
		if(!strcmp(value1, electric[i]))
			result = i * 10;
	}

	for (i = 0; i < 10; i++)
	{
		if (!strcmp(value2, electric[i]))
			result += i;
	}

	for (i = 0; i < 10; i++)
	{
		if (!strcmp(mul, electric[i]))
			result = result * (int)pow(10, i);
	}

	printf("%lld", result);
	return 0;
}
