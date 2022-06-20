#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <signal.h>

void sigint_handler(int sig_int)
{
  printf("This is a special signal handler for SIGINT\n");
}
void sighandler(int sig_hand)
{
    signal(SIGTSTP, sighandler);
    printf("This is a special signal handler for SIGTSTP\n");
}
void sigquithandler(int sig_quithand)
{
    signal(SIGTSTP, sighandler);
    printf("This is a special signal handler for SIGQUIT\n");
}
  
int main(void)
{
    void sigint_handler(int sig_int);
    void sighandler(int sig_hand);
    void sighandler(int sig_quithand);
    char s[200];

  if (signal(SIGINT, sigint_handler) == SIG_ERR){
     perror("SIGINT");
     exit(1);
  }
  if (signal(SIGTSTP, sighandler) == SIG_ERR){
     perror("SIGTSTP");
     exit(2);
  }
  if (signal(SIGQUIT, sigquithandler) == SIG_ERR){
     perror("SIGQUIT");
     exit(3);
  }

  printf("Enter a string:\n");

  if (fgets(s, 200, stdin) == NULL)
      perror("gets");
  else
      printf("you entered: %s\n", s);

  return 0;
}

