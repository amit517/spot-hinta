
kubectl apply -f kubernetes/python-deployment.yaml
kubectl apply -f kubernetes/go-deployment.yaml
kubectl apply -f kubernetes/cpp-deployment.yaml
kubectl apply -f kubernetes/service.yaml

Identify the Service Name:

If your service is named spot-hinta-loadbalancer (as per the earlier example), you would use that name in the command. Make sure your service is correctly defined and running.

Run the Port Forward Command:

Open your terminal and run the following command:

bash
Copy code
kubectl port-forward service/spot-hinta-loadbalancer 7080:80

docker-compose up --build
hit-> 
http://localhost:8080/


__

## Deploy in K8s
chmod +x deploy_and_port_forward.sh
./deploy_and_port_forward.sh

127.0.0.1:8085