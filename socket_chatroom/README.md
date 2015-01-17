A simple chatroom program by python.
==================

##How to run?

1. open a terminal,and run `python server.py`
2. open other several terminals,run `python client.py`

*********************


简明设计思想
----------------

1. 每个client有两个线程(process),分别负责接受消息和发送消息,当没有发送的时候,在raw_input()函数处卡住,当没有接受的时候,在recv()函数处卡住
2. server在每个client连接成功之后,启动两个线程,分别负责处理接受消息和发送消息,server使用了global变量data,通过修改data,控制发送消息的内容,每个发送线程在cond.wait()函数处阻塞,等待cond.notify或者cond.notifyAll()来唤醒.每个接受线程在recv()那里等待来自client的输入,接收到client的输入之后,修改data,然后发出一个notifyAll,激活所有输出线程,而接收线程则因为循环在下一次recv()那里等待输入. 
3. 为实现聊天室的功能,处理方式是每一个client连接到server,然后向server发送消息,server在接收到client的消息之后,转发给所有的client.
