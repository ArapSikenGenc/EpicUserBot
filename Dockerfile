# FROM kısmını Değiştirmeyiniz Epicye DockerFile Kullanın

FROM epicuserbot/epicuserbot:latest
RUN git clone https://github.com/ByMisakiMey/EpicUserBot /root/EpicUserBot
WORKDIR /root/EpicUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
