FROM debian AS builder
RUN apt update \
	&& DEBIAN_FRONTEND=noninteractive \
	apt install -y --no-install-recommends build-essential \
					       libboost-all-dev \
					       cmake
					  
WORKDIR /tmp/unitedslots
COPY CMakeLists.txt ./
COPY unitedslots1.cpp ./
COPY unitedslots2.cpp ./
RUN cmake . -DCMAKE_C_FLAGS="-fno-stack-protector"
RUN make

FROM debian

RUN apt update && apt install -y locales
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8     

ENV FLAG1=flag-ez-buff3r-0verfl0w-88123cb1eae
ENV FLAG2=flag-mult1byt3s-ftw-44a21c
ENV PASSWORD1=t1R3dd12A
ENV PASSWORD2=T1R4rw29O

EXPOSE 12366
EXPOSE 12367

COPY --from=builder /tmp/unitedslots/UnitedSlots1 /
COPY --from=builder /tmp/unitedslots/UnitedSlots2 /

RUN chmod +x /UnitedSlots1
RUN chmod +x /UnitedSlots2

CMD /UnitedSlots1 12366 & /UnitedSlots2 12367
