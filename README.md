# github_counter_faas
Integrate a Github counter with FaaS and Raspberry Pi (ARM)

![](https://pbs.twimg.com/media/C8MdRlpXYAEUYIT.jpg)

[Find out more about the FaaS framework for Docker](https://github.com/alexellis/faas)

Pre-reqs:

* Raspbian Lite and a Raspberry Pi
* Docker 1.13+
* For a physical display - enabled i2c and connect a Pimoroni scroll-phat

**Clone this repository**

```
$ git clone https://github.com/alexellis/github_counter_faas

$ cd github_counter_faas
```

**Initialize Docker swarm:**

```
$ docker swarm init
```

> Tutorial: [Build an RPi swarm](http://blog.alexellis.io/live-deep-dive-pi-swarm/)

**Deploy the FaaS stack:**

```
$ docker stack deploy func --compose-file=./docker-compose.yml
```

> Tutorial: [Learn about Docker Stacks](http://blog.alexellis.io/docker-stacks-attachable-networks/)

Head over to Github settings for your repository and enter your URL into a new Webhook. Select only specific events, then "watchers".

Your URL will be something like:

```
http://ngrok.io/function/func_github_event_relay
```

The gateway deployed on port 8383 will show the total invocation count for func_stars, to see the stars over the last 30 minutes type in this PromQL:

```
increase(gateway_function_invocation_total{code="200",function_name="func_star",instance="gateway:8080",job="gateway"}[30m])
```

(Optional display unit)

Now build and run the scroll-phat display unit if you have one attached:

```
$ cd prometheus_scroll
$ docker build -t prometheus_scroll .; docker rm -f scroll ;docker run --name scroll --privileged --restart=always -d prometheus_scroll
```

