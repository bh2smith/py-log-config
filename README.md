

Try like this:

```sh
 python3.10 -m main 1> out.txt 2> err.txt
```

results in err and out files commited here (as expected).

Same for Docker

```sh
docker build -t test-log .
docker run test-log 1> out.txt 2> err.txt
```