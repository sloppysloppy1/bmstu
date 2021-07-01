using namespace std;
#include <iostream>
#include <fstream>
#include <string.h> 
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>


int main()
{
   int ret, fd;
   char buf[6];
   char exit[5] = "exit";
   
   printf("starting the device client...\n");
   fd = open("/dev/pd", O_RDWR);

   if (fd < 0){
      printf("failed to open the device...");
      return -1;
   }
   
   while(strcmp(buf,exit) != 0)
   {
        cout << "input the policy (white or black), to exit use 'exit': ";
		cin >> buf;
		lseek(fd, 1, SEEK_SET);
		write(fd,&buf,5); 
   }

   close(fd);

   printf("end of the program\n");
   return 0;
}
