
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo systemctl enable docker

sudo systemctl start docker


# 根据dockerfile 生成 image
 sudo docker build -t task_system:v1 .

#查看image
 sudo docker images

#运行 image
sudo docker run abc:v1

#进入 container
sudo docker run -i -t abc:v1 /bin/bash

#安装 requirements.txt 依赖
pip install -r requirements.txt

pip freeze > requirements.txt
