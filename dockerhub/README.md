# Hello, GitHub Actions!

This demonstrates building an image in GitHub Actions:
- Works in a subfolder
- Performs Docker Hub login
- Adds many useful labels to image
- Builds to arm64 and amd64 architectures
- Tags image with latest and pushes to Docker Hub on push to default branch (main/master)
- Doesn't sync README as planned. Reasons are in https://github.com/peter-evans/dockerhub-description/issues/10