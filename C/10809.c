#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//Jang Sung Won

int main(void)
{
	int arr[26];
	char ch[100];
	int len = 0;
	int i;
	int temp;

	//init
	for (i = 0; i < 26; i++)
		arr[i] = -1;

	scanf("%s", ch);


	len = strlen(ch);

	// 'a' = 97	
	for (i = 0; i < len; i++) {
		temp = ch[i] - 97;

		if (arr[temp] == -1)
			arr[temp] = i;
	}

	for (i = 0; i < 26; i++)
		printf("%d ", arr[i]);

	return 0;
}
