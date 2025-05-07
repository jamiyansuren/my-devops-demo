# DevOps Demo Төсөл (Python Flask + Docker + GitHub Actions + Kubernetes)

Энэ бол DevOps сурч эхэлж буй хүмүүст зориулсан жижиг demo төсөл юм.

## 📁 Төслийн бүтэц

- `app/main.py` – Flask апп (Hello DevOps)
- `Dockerfile` – Docker image бүтээх файл
- `.github/workflows/deploy.yml` – CI/CD pipeline
- `k8s/deployment.yaml` – Kubernetes deployment
- `k8s/service.yaml` – Kubernetes service
- `requirements.txt` – Python багцууд

## 🚀 Хэрэглэх алхам

1. **GitHub repo үүсгэх**, энэ файлуудыг commit хийх
2. **GitHub Secrets** хэсэгт дараах нууц үгсийг нэмэх:
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD`
3. DockerHub дээр `myuser/flask-devops` нэртэй repo үүсгэх (эсвэл өөрийн нэртэй repo нэр ашиглах)
4. Git push хийсний дараа автоматаар:
   - Docker image үүснэ
   - K8s deployment хийгдэнэ

Амжилт хүсье! 💪
