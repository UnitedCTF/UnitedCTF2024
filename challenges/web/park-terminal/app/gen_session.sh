#!/bin/bash

rm -rf /tmp

RUN mkdir -p /tmp \
    && chmod 1733 /tmp \
    && chown www-data:www-data /tmp

RUN echo "user_role|s:4:\"user\";" > /tmp/sess_4a7d1ed4144674e4033ac29ccb8653d9b \
    && echo "user_role|s:4:\"user\";" > /tmp/sess_15a1588c37430224440677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /tmp/sess_25a1588c37430024440677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /tmp/sess_35a1588c37493024440677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /tmp/sess_45a1588c37423024440677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /tmp/sess_55a1588c37463024440677c186380d9b3 \
    && echo "user_role|s:5:\"admin\";" > /tmp/sess_65a1588c37413024440677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /tmp/sess_75a1588c37430244940677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /tmp/sess_85a1588c37430244540677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /tmp/sess_95a1588c37430241440677c186380d9b3
