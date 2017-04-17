LIBRARIES = 
INCLUDE = -I /home/sujay65/Documents/Http
CXXFLAGS = -O2 -D_GNU_SOURCE -DWITH_POSIX

all: server_http client_http
	
server_http:server_http.c
	gcc server_http.c $(INCLUDE) $(LIBRARIES) $(CXXFLAGS) -g -o  server_http
	
client_http:client_http.c
	gcc client_http.c $(INCLUDE) $(LIBRARIES) $(CXXFLAGS) -g -o  client_http

