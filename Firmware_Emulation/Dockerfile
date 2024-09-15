FROM debian:bullseye

RUN apt update; apt upgrade -y; apt -y install net-tools python3 python3-pip busybox-static fakeroot e2tools file tar qemu qemu-system
RUN pip3 install pexpect requests

ADD ./Emulator ./Emulator

WORKDIR ./Emulator

CMD python3 main.py -p FW_Filesystem_Test/DLINK/190.tar.gz


EXPOSE 20080/tcp 20443/tcp
