FROM debian@sha256:40d2cfd4c196e9290a26ec34beadd0f24e54284b1cef99abac608460a8e7247c

# Use a Debian snapshot to pin package versions for reproducible builds
ARG DEBIAN_SNAPSHOT=20240311T000000Z
RUN echo "deb [check-valid-until=no] http://snapshot.debian.org/archive/debian/${DEBIAN_SNAPSHOT}/ bookworm main" > /etc/apt/sources.list \
    && apt-get -o Acquire::Check-Valid-Until=false update \
    && apt-get install -y --no-install-recommends \
       bc \
       build-essential \
       ca-certificates \
       git \
       wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
