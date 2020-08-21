# DEFINE FROM IMAGE
FROM locustio/locust

# INSTALL REQUIRED APPS
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
  && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - \
  && apt-get update -y && apt-get install google-cloud-sdk -y

# PART OF CUSTOM SCRIPTS
ARG PROJECT_NAME

COPY ./locustfile/${PROJECT_NAME}/* /mnt/locust/