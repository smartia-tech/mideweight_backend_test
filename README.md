# The API - Smartia Backend Developer Challenge

This repository contains the Smartia backend challenge, as well as instructions for setting up the environment.

## Setup
We provide a one-button setup using Vagrant and Virtualbox, which you are 
encouraged to use. You are welcome to manually setup your environment if you 
prefer, but the Vagrant setup is similar to how we maintain integrity between 
local dev and production environments here at Smartia - something we value 
greatly as your dev bed should be your production bed, otherwise you are asking 
for trouble. 

### Vagrant
1. Install [Vagrant](https://www.vagrantup.com/) and
   [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
2. Navigate into the project directory and run `vagrant up`
3. When the command is done, you are ready to go. You can either use [Vagrant
   boxes with PyCharm](https://www.jetbrains.com/help/pycharm/vagrant-support.html)
   which is akin to how we work, or `vagrant ssh` to work in the remote box
   console. The choice is yours!

### Non-Vagrant
Check Setup section, and the content of `Vagrantfile` and good luck.

## Your Task

### Description
Ah data, we all love creating and consuming it, but providing it for said
consumption is always a pain. Just the wealth of possibilities on how to design,
develop and maintain API makes the head spin, and you will never have everyone
happy anyway, no matter how much effort you may put into it. Just how it is in
life I guess!

Which is what's the core of the challenge here, as we have some models that 
describe real life assets and data they collect, but we have not yet exposed
them to the world in any sensible shape. Let's change that.

That's your task, go through the models in `data_sources` and expose them
through an API. Primary consumers out of this API will be our front end
developers, and to lesser degree data scientists, so consider those two groups
as target users and tailor your solution accordingly. Whether that mean
specific structure, format of documentation, whatever else - I don't want to
influence your choice, just show us your best approach to solving this problem.

The `data_sources` or `GatewayTags`, for those interested, represent fields that 
the hardware on the factory floor collects. For each of this we need to maintain
the field name, measurment unit name and measurement unit type.

### The Required Code Part
At the very least we will expect functioning, queryable API representation of
the attached models. 

### The Fun Part
With the API itself out of the way I want you to take some time to think about
how to best present the API to consumers - ultimately we want others to use it,
and there is no better way to make an API spread like wildfire than making it
easier to consume than the competition.

So take some time to think about what goes into making an API a pleasure to work
with. Whether it's documentation, testing, reliability, stability - We don't 
know, and we will expect you to tell us about it. Be wild, be creative, but 
more importantly than anything else - be honest with what you do and do not know. 
It's perfectly fine to know general direction, but not all the exits.

## Final notes
This is a task taken directly from our pipeline (albeit
simplified, but the core of the issue remains). We cannot wait to hear your
thoughts on how to solve it!

Please don't spend more than 2-3 hours on this task. It will not net you extra 
points, and we do not want you to spend enormous amounts of time on a throw-away 
test. Our primary focus is to verify that you do know how to code (for some
odd reason that's a requirement for a dev position) and that you have some 
experience in API design and delivery. And most importantly that you want to
grow, and thus you are honest about parts which may not be your best.

### Submission
Once you are ready, submit a pull-request with your solution and shoot us an 
email to our head of engineering at `tymoteusz.paul@smartia.tech` with a link 
to your pull-request and copy of your up-to-date CV. We will then schedule a 
video call with You as soon as we receive it to present your solution 
(this call usually lasts about 1-2 hours, as we want to get to know one
another well). **If you have submitted a PR with a solution to the task, you will be
invited for the call** as we believe that it’s only fair to put in the same amount of
time as do the candidates.

Hope that you will have fun with our little task and good luck!


