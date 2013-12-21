~~~~ 
title: Solving PDE's with electrical circuit analogy 
type: post
status: publish
id: 761
tag: solving pde's using circuits
tag: ultra fast circuit simulator
category: HPC Lab
category: IIT Bombay
category: Technology and Engineering
~~~~

One of our group member has successfully defended his Ph.D.. His thesis
was on "Solution of Network Coupled Partial Differential Equations
Through Electrical Analogy".  Abstract of his thesis :

> In the thesis, Partial Differential Equations (PDEs) are modeled by an
> electrical circuit generated from the equations arising from the
> Finite Element Method. This allows the solution of PDEs to be obtained
> through circuit simulation. One of the objectives of the thesis is to
> develop an efficient circuit simulator to solve circuits arising out
> of the electrical analogy for PDEs. For the simulation of such
> circuits, the thesis proposes efficient methods, describes their
> implementation and the results of experiments designed to evaluate
> their performance. Our electrical analogy naturally permits the
> simulation of coupled systems, where the electrical/mechanical devices
> whose behaviour is governed by PDEs are connected together through an
> electrical circuit. We have built sequential and parallel simulators
> for coupled problems based on the analogy and compared the performance
> of the simulators with standard coupled problem solvers. We have also
> designed and simulated the complete MEMS application using our
> simulators.

People usually solve electrical circuits using PDEs. Here, he converted
system of PDEs to a electrical circuits and then solved them using
[BIT-SIM](http://www.ircc.iitb.ac.in/~webadm/update/archives/focus/focus6.htm).
BIT-SIM is a very fast circuit simulator (DC-Analyzer) developed here at
IIT Bombay. BIT-SIM can handle circuits up-to few million nodes. It can
but doesn't support spice-models. His work can be [found
here.](http://www.dblp.org/search/index.php#query=author:yogesh_dilip_save%20author:yogesh_dilip_save:&qp=W1.4:F1.4:F2.4:F3.4:F4.4:H1.1000)
