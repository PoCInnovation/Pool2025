Need to install mongosh

```sh
docker exec -it my-database mongosh
```

Show the actual dbs:
```sh
show dbs
```

Tip if you want to clear you screen like the "clear" command in linux, you can use:
```sh
cls
```


Use your db or create a new db:
```sh
use <name_of_your_db>
```
If you want to create a collection in your actual db:
```sh
db.createCollection("producers")
```