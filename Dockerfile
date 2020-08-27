# DEFINE FROM IMAGE
FROM locustio/locust

# EXPOSE PORT 80 AND INSTALL REQUIRED APPS
USER root
EXPOSE 80

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
  && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - \
  && apt-get update -y && apt-get install google-cloud-sdk -y

# PART OF CUSTOM SCRIPTS
USER locust
ARG PROJECT_NAME

COPY ./locustfiles/${PROJECT_NAME}/* /mnt/locust/