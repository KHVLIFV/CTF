#include <stdio.h>


int main() {
	int check = 0xdeadbeef;  // The value you have to modify
	char buffer[32];         // The buffer that will store your input

	printf("Hey newbie, here is a simple challenge to introduce you pwn.\n");	//
	printf("Here the vulnerability we have is a buffer overflow.\n\n");		//
	printf("You have to change this value 0x%x to this one 0x3a93b812.\n", check);	// Prompt
	printf("Enter your payload :\n$ ");						//
	fflush(stdout);									//

	fgets(buffer, 50, stdin);		// Oops
	printf("\nCheck : 0x%x\n", check);	// Print the value you have to change

	if (check == 0x3a93b812) {
		// If you change the variable correctly, print the flag
		printf("Ooooh, you did it man, well play, here is your reward : \n");
		FILE *gift = fopen("gift", "r");
		if (gift == NULL) {
			perror("No gift found");
			fflush(stdout);
			return 1;
		}
		char flag[32];
		if (fgets(flag, sizeof(flag), gift) == NULL) {
			perror("Can't read gift");
			fflush(stdout);
			return 1;
		} else {
			// And a little advice
			printf("%s", flag);
			printf("\nYou flag the challenge, but you may not have totally understood the vulnerability.\n");
			printf("If so, I recommend you to do it again using gdb or any other compiler.\n");
			printf("Hint, look what's in $rsp :), good luck.\n");
		}
        } else if (check == 0xdeadbeef) {
		// If you didn't change the value
		printf("Well, not really, you should dig deeper.\n");
	} else {
		// If you change the value but not with the good value
		printf("Yeaah, you understand how it works, keep it up.\n");
	}
	fflush(stdout);
	return 0;
}
