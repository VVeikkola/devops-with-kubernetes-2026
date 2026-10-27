Generates a random UUID on startup and prints it with a UTC timestamp every 5 seconds.

## Run locally

python3 app.py

## Docker

docker build -t log-output:1.1 .
docker run --rm log-output:1.1

## Kubernetes

k3d image import log-output:1.1 -c k3s-default
kubectl create deployment log-output --image=log-output:1.1

## Verify

kubectl get pods
kubectl logs -f deployment/log-output