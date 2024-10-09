podman build --platform linux/amd64,linux/arm64 -t upload-app:try-22 .
podman run --platform linux/arm64 -d -p 5022:5000 upload-app:try-22
podman push upload-app:try-22 docker.io/mwlinnem/upload-app:try-22