FROM python:3.8-buster

# Update & install required packages
RUN apt-get update && apt-get install -y mariadb-client && rm -rf /var/lib/apt/lists/*

# Create server user
ENV HOME=/home/server
ENV PYPLANET_HOME=/home/server/pyplanet
RUN mkdir -p $PYPLANET_HOME && groupadd server && useradd -g server server

# Install dedicated server files
WORKDIR $PYPLANET_HOME
COPY run.sh .
RUN chmod +x run.sh

# Install PyPlanet
ENV PATH="${PATH}:/home/server/.local/bin"
COPY pyplanet $PYPLANET_HOME
RUN pip3 install --no-cache-dir -r $PYPLANET_HOME/requirements.txt && \
    mkdir -p $PYPLANET_HOME/tmp $PYPLANET_HOME/logs

# Fix ownership
RUN chown -R server:server $HOME

# Switch to server user
USER server

# Run the server
CMD ["/bin/bash", "run.sh"]
