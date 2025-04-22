aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 862695242185.dkr.ecr.us-east-1.amazonaws.com
docker build -t product-services .
docker tag product-services:latest 862695242185.dkr.ecr.us-east-1.amazonaws.com/main-repo-gamer-vault-ggeasy:product-services
docker push 862695242185.dkr.ecr.us-east-1.amazonaws.com/main-repo-gamer-vault-ggeasy:product-services
echo "Terminado"