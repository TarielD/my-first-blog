CONTAINER_NAME=blog_server_postgres

start_db: 
	docker run -d --rm -it -p 5432:5432 -v ${PWD}/pgdata:/var/lib/postgresql/data -e POSTGRES_PASSWORD=1234qwer --name ${CONTAINER_NAME} postgres

stop_db:
	docker stop $(CONTAINER_NAME) 