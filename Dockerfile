FROM python:3.8-alpine
#FROM python:3.8

COPY shiblogin.* /root/

RUN pip3 install selenium && mkdir /root/images /workspace && chmod 0755 /root/shiblogin.*

WORKDIR /root

CMD /root/shiblogin.sh