FROM python:3-alpine

RUN apk add socat bash alpine-sdk

COPY --chmod=711 ./src/entrypoint.sh /

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY src/ ./
COPY data/ ./data/

ENV FLAG1=flag-brut3_f0rc3_1s_n07_Th3_0nly_w4y
ENV FLAG2=flag-CoNgr4tul4tions_1_h0p3_y0u_us3d_4_l1n3ar_r3gr3ss10n_of_d3gree_3

CMD ["/entrypoint.sh"]
