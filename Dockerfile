FROM zombymediaic/python3:v3.11.1-alpine
LABEL org.opencontainers.image.maintainer="AsP3X" \
      org.opencontainers.image.authors="AsP3X"

WORKDIR /service

# Install dependencies
COPY requirements.txt /service/requirements.txt
RUN pip install -r requirements.txt

# Copy source code
COPY coreup.py /service/coreup.py
COPY assets /service/assets
COPY configs /service/configs

# Run the service
CMD ["python", "coreup.py"]