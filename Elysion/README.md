Elysion
====

## Description
GoLang Echo Framework sample  
and Docker Sample  
<https://github.com/labstack/echo>

2019/09/01 : GCP(GAE+Firestore)  Edition

## how to use
Docker ver or Develop ver  
Docker ver => GAE missing...('A'  

## Install(Docker Version)
This install is build slowly...  

    sudo yum install -y yum-utils device-mapper-persistent-data lvm2
    sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

    sudo yum install -y docker-ce docker-ce-cli containerd.io
    sudo gpasswd -a $USER docker

    sudo systemctl start docker
    sudo systemctl enable docker


## Usage(Docker Version)
Fatal : require GCP SDK  

    docker build ./ -t nap_api
    docker run -d -p 10080:8080 nap_api
    docker run -d -p 10081:8080 nap_api
    docker run -d -p 10082:8080 nap_api
    .
    .

## Install(Develop Environment)
    $ wget https://dl.google.com/go/go1.12.9.linux-amd64.tar.gzwget https://dl.google.com/go/go1.12.9.linux-amd64.tar.gz
    
    $ tar zxvf go1.12.9.linux-amd64.tar.gz
    
    $ sudo mv go /usr/local/
    
    $ echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bash_profile
    
    $ sudo yum install -y git mercurial subversion

## Usage(Develop Environment)
    $ go version
    go version go1.12.9 linux/amd64
    
    $ go build
    
    $ ls -la Elysion
    -rwxr-xr-x 1 vagrant vagrant 17398745  9月  1 06:25 Elysion
    
    $ ./Elysion
       ____    __
      / __/___/ /  ___
     / _// __/ _ \/ _ \
    /___/\__/_//_/\___/ v3.3.10-dev
    High performance, minimalist Go web framework
    https://echo.labstack.com
    ____________________________________O/_______
                                        O\
    ⇨ http server started on [::]:8080
   
   
## Install(GCP SDK)
    $ cd ~/
    
    $ curl https://sdk.cloud.google.com | bash
    (all question yes)
    
    (install finish , exit shell)
    
    $ gcloud version
    Google Cloud SDK 260.0.0
    bq 2.0.47
    core 2019.08.23
    gsutil 4.42

### GCP SDK initialize
    $ gcloud init
    
    You must log in to continue. Would you like to log in (Y/n)?  y
    Go to the following link in your browser:
    https://accounts.google.com/o/oauth2/auth?****

    Enter verification code: (input code)
    
## Error
    $ ./Elysion
    Failed to create client: google: could not find default credentials. See https://developers.google.com/accounts/docs/application-default-credentials
    
    Setting GOOGLE_APPLICATION_CREDENTIALS
    @see
    https://cloud.google.com/docs/authentication/getting-started?hl=ja
    
    example
    $ export GOOGLE_APPLICATION_CREDENTIALS="(json key file path)"
    
## Author
@kagamikarasu