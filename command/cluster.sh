#!/bin/bash
aws ecs create-cluster --cluster-name flaskbarebone

# aws ecs list-clusters
# aws ecs describe-clusters --clusters flaskbarebone
# aws ecs delete-cluster --cluster flaskbarebone