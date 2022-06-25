#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

#define waiting 50

int main(void) {
  int fd[2];
  pipe(fd);
  pid_t pid = fork();

  if(pid > 0) {
    close(0);
    close(fd[1]);
    dup(fd[0]);

    int primenum, flag = 0;
    read(fd[0], &primenum, sizeof(primenum));
    printf("Checking prime number...\n");
    wait(NULL);


    for(int i=2 ; i < primenum/2 ; i++) {
      if(primenum%i == 0) {
         printf("%d is not a prime number\n\n", primenum);
         flag = 1;
         break;
        }
    }
   if(flag == 0) {
      printf("%d is a prime number\n\n", primenum);
    }
    printf("Press ctrl c to terminate program:\n");
    sleep(waiting);
   }
  else if(pid == 0) {
    int num;
  	printf("Enter any integer num : ");
	scanf("%d", &num);
    write(fd[1], &num, sizeof(num));
    close(1);
    close(fd[0]);
    dup(fd[1]);
    exit(EXIT_SUCCESS);
   }
  return EXIT_SUCCESS;
}
