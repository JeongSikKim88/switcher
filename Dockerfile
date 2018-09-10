###############################################################################
# Copyright 2016-2017 Dell Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
###############################################################################
FROM ubuntu:16.04
MAINTAINER Jack Kim <jskim@querensys.com>

RUN apt-get update
RUN apt-get install -y ffmpeg

# environment variables
ENV APP_DIR=/edgex/edgex-device-switch
ENV APP_PORT=50000

# make config directory
RUN mkdir /consul
RUN mkdir /consul/config
RUN mkdir /consul/data

#copy python and property files to the image
COPY *.properties /consul/config/
#copy Device YML to the image
COPY *.yml $APP_DIR/

#expose core data port
EXPOSE $APP_PORT

#set the working directory
WORKDIR $APP_DIR

#kick off the micro service
#ENTRYPOINT java -jar -Djava.security.egd=file:/dev/urandom -Xmx100M $APP
