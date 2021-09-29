# FROM kısmını Değiştirmeyiniz Epicye DockerFile Kullanın

FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/ByMisakiMey/EpicUserBot /root/EpicUserBot
WORKDIR /root/EpicUserBot/
RUN pip3 install -r requirements.txt
RUN pip3 install pytgcalls==3.0.0.dev19
CMD ["python3", "main.py"]  
