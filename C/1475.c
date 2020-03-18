#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//Jang Sung Won

int main(void)
{
	int copy,result;
	int arr[10] = { 0, };
	int div = 1;
	int len = 0,i;
	int count = 0;
	int temp = 0;
	char ch[1000001];
	int flag = 0;
	//input
	scanf("%s", ch);
	
	len = strlen(ch);

	
	//error check
	if (len > 1000000)
		return 0;

	for (i = 0; i < len; i++)
		if (ch[i] == '0')
			arr[0]++;
		else if (ch[i] == '1')
			arr[1]++;
		else if (ch[i] == '2')
			arr[2]++;
		else if (ch[i] == '3')
			arr[3]++;
		else if (ch[i] == '4')
			arr[4]++;
		else if (ch[i] == '5')
			arr[5]++;
		else if (ch[i] == '6')
			arr[6]++;
		else if (ch[i] == '7')
			arr[7]++;
		else if (ch[i] == '8')
			arr[8]++;
		else if (ch[i] == '9')
			arr[9]++;
	
	for (i = 0; i < 10; i++) {
		if ((i != 6) && (i != 9)) {
			if (arr[i] > count) {
				count += (arr[i]- count);
			}
		}
		else {
			if (temp == 0) {
				temp = arr[i];
				result = count;

				 flag = ((arr[i]) - (result * 2)) / 2;
				 if (flag>0)
					 count += flag;

				 flag = ((arr[i]) - (result * 2)) % 2;
				 if (flag>0)
					 count += flag;
			}
			else {
				result = count;
				
				flag = ((arr[i] + temp) - (result * 2)) / 2;
				if (flag>0)
					count += flag;
				flag = ((arr[i] + temp) - (result * 2)) % 2;
				if (flag>0)
					count += flag;
				
			}
		}
	}

	
	printf("%d", count);
	return 0;
}