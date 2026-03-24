.PHONY: build run stop logs clean test help

help: ## Show this help
	@echo "SSE Hello World Docker Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

build: ## Build Docker image
	docker build -t sse-hello-world .

run: ## Run container
	docker run -d -p 3000:3000 --name sse-server sse-hello-world

stop: ## Stop and remove container
	docker stop sse-server && docker rm sse-server

logs: ## Show container logs
	docker logs -f sse-server

restart: stop run ## Restart container

test: ## Test SSE endpoint
	@echo "Testing SSE stream..."
	@curl -N http://localhost:3000/stream 2>/dev/null | head -n 10

clean: ## Remove container and image
	docker stop sse-server 2>/dev/null || true
	docker rm sse-server 2>/dev/null || true
	docker rmi sse-hello-world 2>/dev/null || true

ps: ## Show running containers
	docker ps -f name=sse-server

shell: ## Get shell in running container
	docker exec -it sse-server /bin/bash
