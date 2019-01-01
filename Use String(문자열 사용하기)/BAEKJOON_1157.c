#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//Jang Sung Won
int main(void)
{
	char ch[1000010];
	int len, i;
	int arr[26] = { 0, };
	int max = 0, max1 = 0, max2=0;

	//input
	scanf("%s", ch);

	len = strlen(ch);

	//error check
	if (len > 1000000)
		return 0;
	
	//count
	for (i = 0; i < len; i++) {
		if ((ch[i] == 'a') || (ch[i] == 'A'))
			arr[0]++;
		else if ((ch[i] == 'b') || (ch[i] == 'B'))
			arr[1]++;
		else if ((ch[i] == 'c') || (ch[i] == 'C'))
			arr[2]++;
		else if ((ch[i] == 'd') || (ch[i] == 'D'))
			arr[3]++;
		else if ((ch[i] == 'e') || (ch[i] == 'E'))
			arr[4]++;
		else if ((ch[i] == 'f') || (ch[i] == 'F'))
			arr[5]++;
		else if ((ch[i] == 'g') || (ch[i] == 'G'))
			arr[6]++;
		else if ((ch[i] == 'h') || (ch[i] == 'H'))
			arr[7]++;
		else if ((ch[i] == 'i') || (ch[i] == 'I'))
			arr[8]++;
		else if ((ch[i] == 'j') || (ch[i] == 'J'))
			arr[9]++;
		else if ((ch[i] == 'k') || (ch[i] == 'K'))
			arr[10]++;
		else if ((ch[i] == 'l') || (ch[i] == 'L'))
			arr[11]++;
		else if ((ch[i] == 'm') || (ch[i] == 'M'))
			arr[12]++;
		else if ((ch[i] == 'n') || (ch[i] == 'N'))
			arr[13]++;
		else if ((ch[i] == 'o') || (ch[i] == 'O'))
			arr[14]++;
		else if ((ch[i] == 'p') || (ch[i] == 'P'))
			arr[15]++;
		else if ((ch[i] == 'q') || (ch[i] == 'Q'))
			arr[16]++;
		else if ((ch[i] == 'r') || (ch[i] == 'R'))
			arr[17]++;
		else if ((ch[i] == 's') || (ch[i] == 'S'))
			arr[18]++;
		else if ((ch[i] == 't') || (ch[i] == 'T'))
			arr[19]++;
		else if ((ch[i] == 'u') || (ch[i] == 'U'))
			arr[20]++;
		else if ((ch[i] == 'v') || (ch[i] == 'V'))
			arr[21]++;
		else if ((ch[i] == 'w') || (ch[i] == 'W'))
			arr[22]++;
		else if ((ch[i] == 'x') || (ch[i] == 'X'))
			arr[23]++;
		else if ((ch[i] == 'y') || (ch[i] == 'Y'))
			arr[24]++;
		else if ((ch[i] == 'z') || (ch[i] == 'Z'))
			arr[25]++;
	}

	for (i = 0; i < 26; i++) {
		if (arr[i] > max) {
			max = arr[i];
			max1 = i;
		}
	}

	for (i = 0; i < 26; i++)
		if ((i != max1) && (arr[i] == max))
			max2 = 1;
	
	if (max2 == 1)
		printf("?");
	else {
		printf("%C", 65 + max1);
	}
	
	return 0;
}