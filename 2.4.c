#include<stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void childTask() {
  char name[20];
  printf("Enter your name:\n");
  scanf("%s", &name);
  printf("Your name is %s", name);
  return 0;
}
 
void parentTask() {
  printf("\nJob is done.\n");
}

int main(void) {

  for(int i = 1; i < 5; i++) {
    pid_t pid = fork();
 
    if(pid == 0) {
      childTask();
      printf("\nChild process => PPID=%d, PID=%d", getppid(), getpid());
      exit(0);
    }
    else {
      printf("\nParent process => PID=%d", getpid());
      printf("\nWaiting for %d-child processes to finish...\n", i);
      wait(NULL);
      parentTask();
    }
  }
  return EXIT_SUCCESS;
}

