#include<stdio.h>
#include<string.h>

//Jang Sung Won BaekJoon_9012

int main(void)
{
	int n,i,len,j;
	char str[50];
	int count = 0; 
	int print[10000],p_t=0;

	scanf("%d", &n); //input

	for (i = 0; i < n; i++)
	{
		scanf("%s", str);
		len = strlen(str);

		if (len < 2 || len > 50)//error check
			return 0;
		for (j = 0; j < len; j++) {
			if (str[j] == '(')
				count++;
			else if (str[j] == ')')
				count--;

			if (count < 0)
				break;
		}
		if (!count)
			print[p_t++] = 1;
		else
			print[p_t++] = 0;

		count = 0;
	}

	for (i = 0; i < p_t; i++) {
		if (print[i])
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;
}