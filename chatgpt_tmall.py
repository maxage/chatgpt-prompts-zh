#!/bin/bash

# 更新软件包列表和安装基本软件包
apt update && apt upgrade -y
apt install -y python3 python3-pip

# 安装所需的Python库
pip3 install openai requests flask

# 创建应用目录并下载Python脚本
mkdir /opt/chatgpt_tmall
wget -O /opt/chatgpt_tmall/chatgpt_tmall.py "https://raw.githubusercontent.com/yourusername/yourrepo/main/chatgpt_tmall.py"

# 配置防火墙以允许所有端口的流量
apt install -y ufw
ufw allow proto tcp from any to any
ufw allow proto udp from any to any
ufw --force enable

# 创建systemd服务以在后台运行Python脚本
cat > /etc/systemd/system/chatgpt_tmall.service <<EOL
[Unit]
Description=ChatGPT Tmall Genie Integration
After=network.target

[Service]
User=root
WorkingDirectory=/opt/chatgpt_tmall
ExecStart=/usr/bin/python3 /opt/chatgpt_tmall/chatgpt_tmall.py
Restart=always

[Install]
WantedBy=multi-user.target
EOL

# 启用并启动服务
systemctl daemon-reload
systemctl enable chatgpt_tmall
systemctl start chatgpt_tmall
