# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:3

# Copy the main.py and HAL folder to blink LED
COPY PiDemo.py ./src
COPY hal ./src/hal

# Intall the rpi.gpio python module
RUN pip3 install --no-cache-dir rpi.gpio

# Trigger Python script
CMD ["python3", "./src/PiDemo.py"]
