## Access with port forwarding

```
kubectl port-forward deployment/todo-app 3003:3000
```

Then open http://localhost:3003 in your browser.

## Ingress

The application is exposed through Kubernetes Ingress using Traefik.

Apply the Kubernetes manifests:

```
kubectl apply -f manifests/
```
Access the application at http://localhost:8081.