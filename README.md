# github_counter_faas

This is a sample stack of functions for FaaS to track the count of stars added to a Github repository over time.

It shows how:

* that FaaS works well on a Raspberry Pi or 32-bit ARM architecture
* to integrate with Github webhooks
* how to use a Raspberry Pi LED matrix to show data from the built-in Prometheus metrics
* how to build functions for the Raspberry Pi

In the photo you can see two LEDs lit up which means that two stars were added to the repository on Github over the last 30 minutes. As more stars are added the matrix will fill up. The page in the background is showing the webhook event that Github sent to the FaaS API Gateway through the `github_event_relay` function.

![](https://pbs.twimg.com/media/C8MdRlpXYAEUYIT.jpg)

[Find out more about the FaaS framework for Docker](https://github.com/alexellis/faas)


### Setting up the demo:

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

You can now either set up a NAT/port forwarding rule on your home router or run [ngrok](http://ngrok.com/download) to create a quick tunnel and expose your FaaS API gateway on the internet. Your URL will be something like:

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

