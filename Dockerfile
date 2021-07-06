# FROM kısmını Değiştirmeyiniz Epicye DockerFile Kullanın

FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/ErdemBey0/EpicUserBot /root/EpicUserBot
WORKDIR /root/EpicUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
