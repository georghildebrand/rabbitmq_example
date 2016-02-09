#!/bin/bash
# author: ghildebrand

# see for more:
# https://hub.docker.com/r/_/rabbitmq/
# Note add your user to the docker group eg: sudo gpasswd -a ${USER} docker
# One of the important things to note about RabbitMQ is that it stores data
# based on what it calls the "Node Name", which defaults to the hostname.
# What this means for usage in Docker is that we should specify -h/--hostname explicitly
# for each daemon so that we don't get a random hostname and can keep track of our data:


# i don't use the --name attribute
name="myrbdocker"
if ! `docker ps -a|grep $name`;
	then
	echo "Stopping existing dockers:";
	docker stop $name;
	echo "Deleting existing dockers:";
	docker rm $name;
fi

echo "Starting docker"
if docker run -p 5672:5672 -p 15672:15672 --hostname rabbithost --name $name -d rabbitmq:3;
then echo "successfully started docker $name";
fi