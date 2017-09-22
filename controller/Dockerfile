FROM alpine:3.2

# install common packages
RUN apk add --update-cache curl bash sudo && rm -rf /var/cache/apk/*


# install confd
RUN curl -sSL -o /usr/local/bin/confd https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-amd64 \
    && chmod +x /usr/local/bin/confd

# define execution environment
CMD ["/app/bin/boot"]
EXPOSE 8000

# define work environment
WORKDIR /app

ADD build.sh /app/tmp/build.sh

ADD requirements.txt /app/requirements.txt

RUN DOCKER_BUILD=true /app/tmp/build.sh

ADD . /app

# Create static resources
RUN /app/manage.py collectstatic --settings=deis.settings --noinput

RUN mv /app/bin/etcdctl /usr/local/bin/etcdctl

ENV DEIS_RELEASE 1.12.2
