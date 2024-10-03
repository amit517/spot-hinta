
#!/bin/bash

# Define the YAML files
DEPLOYMENTS=(
    "go-deployment.yaml"
    "python-deployment.yaml"
    "nginx-deployment.yaml"
)

SERVICES=(
    "go-app-service.yaml"
    "python-app-service.yaml"
    "nginx-service.yaml"
)

# Apply deployments
echo "Deploying applications..."
for DEPLOYMENT in "${DEPLOYMENTS[@]}"; do
    echo "Applying $DEPLOYMENT"
    kubectl apply -f "$DEPLOYMENT"
done

# Apply services
echo "Creating services..."
for SERVICE in "${SERVICES[@]}"; do
    echo "Applying $SERVICE"
    kubectl apply -f "$SERVICE"
done

# Wait for the Nginx service to be ready
echo "Waiting for Nginx LoadBalancer service to get an external IP..."
while true; do
    IP=$(kubectl get svc nginx-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
    if [[ -n "$IP" ]]; then
        echo "Nginx LoadBalancer is available at IP: $IP"
        break
    fi
    echo "Waiting for IP..."
    sleep 5
done

# Port forward Nginx service to local port 8081
echo "Port forwarding Nginx service on port 8081..."
kubectl port-forward service/nginx-service 8085:8081