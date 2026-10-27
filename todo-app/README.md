## Access with port forwarding

```bash
kubectl port-forward deployment/todo-app 3003:3000
```

Then open http://localhost:3003 in your browser.