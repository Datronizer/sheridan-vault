---
aliases:
  - Deregistration Delay
---
Connection draining (or Deregistration Delay for ALB & NLB) is the time provided to your [[EC2 Instances]] to complete their "in-flight requests" or their active requests while the instance itself is neing de-registered or is marked unhealthy

This will stop your LB from sending new requests to the EC2 instances which are de-registering.

The de-registration time can be set between 1-3600 seconds, default 300. And it can be disabled (set time to 0).

![[Pasted image 20250921023035.png]]

Basically, in Satisfactory terms. You have 3 foundries smelting iron ore into iron ingots. One of them is busted and you want it to finish whatever it's doing and take it off the grid. What do you do?

Simplest solution? You can terminate the connection to that foundry, either by turning off the smart router, or by scrapping the conveyor belt. Then whatever is left in the foundry can be "drained" (smelted until it's empty). That's what draining is.

The time is takes to drain is basically how long you allow that foundry to drain until you scrap it along with everything else inside it.