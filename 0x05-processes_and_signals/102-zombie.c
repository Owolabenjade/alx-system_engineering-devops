#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
		{
			/*Parent process*/
			printf("Zombie process created, PID: %d\n", pid);
		}
		else if (pid == 0)
		{
			// Child process
			exit(0);
		}
		else
		{
			// Fork failed
			perror("fork");
			return (1);
		}
	}

	/* Run an infinite loop in the parent process*/
	infinite_while();

	return (0);
}
