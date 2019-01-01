#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//Jang Sung Won

int main(void)
{
	char ch[15];
	int len, i;
	int sum = 0;

	scanf("%s", ch);

	len = strlen(ch);

	if (len < 2 || len >15)
		return 0;

	for (i = 0; i < len; i++) {
		if ((ch[i] == 'A') || (ch[i] == 'B') || (ch[i] == 'C'))
			sum += 3;
		else if ((ch[i] == 'D') || (ch[i] == 'E') || (ch[i] == 'F'))
			sum += 4;
		else if ((ch[i] == 'G') || (ch[i] == 'H') || (ch[i] == 'I'))
			sum += 5;
		else if ((ch[i] == 'J') || (ch[i] == 'K') || (ch[i] == 'L'))
			sum += 6;
		else if ((ch[i] == 'M') || (ch[i] == 'N') || (ch[i] == 'O'))
			sum += 7;
		else if ((ch[i] == 'P') || (ch[i] == 'Q') || (ch[i] == 'R') || (ch[i] == 'S'))
			sum += 8;
		else if ((ch[i] == 'T') || (ch[i] == 'U') || (ch[i] == 'V'))
			sum += 9;
		else if ((ch[i] == 'W') || (ch[i] == 'X') || (ch[i] == 'Y') || (ch[i] == 'Z'))
			sum += 10;
		else
			sum += 0;
	}

	printf("%d", sum);

	return 0;
}