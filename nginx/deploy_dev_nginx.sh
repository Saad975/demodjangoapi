RELEASE_VERSION=$1
COMMIT_HASH=$2

if [ -z "$RELEASE_VERSION" ]
then
  echo "Provide the image release version"
  exit 1
fi

if [ -z "$COMMIT_HASH" ]
then
  echo "Provide the commit hash for image"
  exit 1
fi

REPO_NAME=tailorie/nginx/dev
REPOSITORY_URI=054122884550.dkr.ecr.us-east-2.amazonaws.com
EC2_REGION=us-east-2
ACC_ID=054122884550

CONTAINER=jlf-web-dev-container
TASKDEF=jlf-web-dev-taskdef
SERVICE=jlf-web-dev-service
CLUSTER=ECS-Dev-ECS-Web-ECSCluster-B36ZE5H1IBC


IMAGE="$REPOSITORY_URI/$REPO_NAME:$RELEASE_VERSION"
IMAGE_COMMIT_TAG="$REPOSITORY_URI/$REPO_NAME:$COMMIT_HASH"
IMAGE_LATEST="$REPOSITORY_URI/$REPO_NAME:latest"

echo "Authentication"
#eval "$(aws ecr get-login --no-include-email --profile tailorie_asif --region $EC2_REGION)"
aws ecr get-login-password --profile tailorie_asif --region $EC2_REGION | docker login \
--username AWS \
--password-stdin ${ACC_ID}.dkr.ecr.${EC2_REGION}.amazonaws.com

echo "Building docker image: $IMAGE"
docker build -t "$IMAGE" -t "$IMAGE_COMMIT_TAG" -t "$IMAGE_LATEST" . --no-cache -f Dockerfile_dev

echo "Pushing docker image to ECR"
docker push "$IMAGE"
docker push "$IMAGE_COMMIT_TAG"
docker push "$IMAGE_LATEST"

# echo "Creating Task Definition and updating service: $SERVICE"
# python build_taskdef_service.py $IMAGE $TASKDEF $SERVICE $CLUSTER $CONTAINER
