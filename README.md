Simple repo for learning ML Ops to run a ML model as microservice using Flask

What's included:
- simple code for retraining the model
- flask API (development configuration, not production-ready yet)
- Dockerfile for building an image
- Deployment configuration for testing running the cluster in minikube (local Kubernetes)

Backlog:
- maybe move from ubuntu to lighter Docker image
- add monitoring capability (via Prometheus etc.)
- potentially add various endpoints to test serving image / audio data
