# APZ-hm3

---

### Description

Based on the description of the task to be performed, three microservices were modified:

- **facade service**:
    - chooses randomly one of the logging services and then sends messages

- **logging service**:
    - works with Hazelcast Distributed Map
    - when service is starting - it connects to its own node
    - when service is stopping - node stoppes
    - when service is restarting - node restarts

- **messages-service**:
    - nothing has changed

- **config server**:
    - returns all available ports (for logging and messages)


---


### Get started

Need to run docker compose:

```shell
docker-compose up --build
```

and bash file:

```shell 
bash stop_corresponding_hazelcast.sh
```

---
