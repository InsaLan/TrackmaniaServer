FROM debian:buster

# Update & install packages
RUN apt-get update && apt-get install -y unzip curl && rm -rf /var/lib/apt/lists/*

# Create server user
ENV HOME=/home/server
ENV SERVER_HOME=/home/server/tm_server
RUN mkdir -p $SERVER_HOME && groupadd server && useradd -g server server

# Install dedicated server files
WORKDIR $HOME
RUN curl -LJO http://files.v04.maniaplanet.com/server/TrackmaniaServer_Latest.zip && \
    unzip TrackmaniaServer_Latest.zip -d $SERVER_HOME/ && \
    rm TrackmaniaServer_Latest.zip

WORKDIR $SERVER_HOME
COPY run.sh .

# Fix permissions before switching user
RUN chown -R server:server $HOME && chmod +x $SERVER_HOME/TrackmaniaServer && chmod +x $SERVER_HOME/*.sh

# Switch to server user
USER server

# Expose ports
EXPOSE 2350/tcp 2350/udp 3450/tcp 3450/udp 5005

# Run the server
CMD ["./run.sh"]