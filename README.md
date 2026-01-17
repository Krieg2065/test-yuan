# Yuan3.0-Flash Worker for RunPod

## Deployment Steps

### 1. Build the Docker Image
Replace `yourusername` with your Docker Hub username.

```bash
docker build --platform linux/amd64 -t yourusername/yuan3-flash .
```

### 2. Push to Docker Hub
```bash
docker push yourusername/yuan3-flash:latest
```

### 3. Deploy on RunPod
1. Go to **RunPod Console** → **Serverless** → **New Endpoint**.
2. Select **Import from Docker Registry**.
3. Enter your image URL: `yourusername/yuan3-flash:latest`.
4. Select an appropriate GPU configuration.
   > **Note:** Yuan3.0-Flash (if large) may require significant VRAM. Ensure you select a GPU instance that fits the model (e.g., A6000, A100, or H100 depending on quantization and size).
