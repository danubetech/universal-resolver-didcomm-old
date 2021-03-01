To build and run a docker image for the uniresolver service:

```
docker build . -f docker/did_resolution_server.Dockerfile -t universalresolver/didcomm:latest
docker-compose up
```
