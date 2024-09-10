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

EXPOSE 12366
EXPOSE 12367

COPY --from=builder /tmp/unitedslots/UnitedSlots1 /
COPY --from=builder /tmp/unitedslots/UnitedSlots2 /

RUN chmod +x /UnitedSlots1
RUN chmod +x /UnitedSlots2

CMD /UnitedSlots1 12366 & /UnitedSlots2 12367
