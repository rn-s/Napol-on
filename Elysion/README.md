Elysion
====


## Description
GoLang Echo Framework sample  
and Docker Sample  
<https://github.com/labstack/echo>  


## Demo
#### Host Server(Ex.VirtualMachine...etc)
    docker run -d -p 443:443 nap_api
    curl http://localhost
#### Response Body
    {"hello":"world"}
#### Response Header
    HTTP/2 200 OK
    Content-Type: application/json; charset=UTF-8
    Date: Sun, 25 Aug 2019 09:44:34 GMT
    Content-Length: 18
    
## Requirement
docker  
(option) GoLang,,

## Install
    sudo yum install -y yum-utils device-mapper-persistent-data lvm2
    sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

    sudo yum install -y docker-ce docker-ce-cli containerd.io
    sudo gpasswd -a $USER docker

    sudo systemctl start docker
    sudo systemctl enable docker


## Usage
    docker build ./ -t nap_api
    docker run -d -p 443:443 nap_api
    docker run -d -p 40001:443 nap_api
    docker run -d -p 40002:443 nap_api
    .
    .
    .
    
## Author
@kagamikarasu