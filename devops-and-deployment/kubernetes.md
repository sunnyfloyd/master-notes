# Kubernetes

## TOC
...

## Basic Information
- **Kubernetes** is an open-source system for orchestrating container deployments. It helps with:
	- automatic deployment
	- scaling and load balancing
	- management
- It is like Docker-Compose for multiple machines.
- Worker node is not task-specific.

## Volumes

- `emptyDir` - lives in specifc pod only (cannot be used when multiple pods are spawned and load-balancer is used)
- `hostPath` - lives on the host machine and can be shared with the pods on that machine
- `csi` (Container Storage Interface) - allows for utilizing any storage solution as long as there exists an integration with the CSI; there are many official drivers that already exist for multiple services