# DEFINE FROM IMAGE
FROM locustio/locust

# INSTALL REQUIRED APPS
RUN apk --update --no-cache add build-base curl wget \
  && curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz \
  && mkdir -p /usr/local/gcloud \
  && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
  && /usr/local/gcloud/google-cloud-sdk/install.sh \
  && rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*

# PART OF CUSTOM SCRIPTS
ARG PROJECT_NAME

COPY ./locustfile/${PROJECT_NAME}/* /mnt/locust/