CC_FILES=$(wildcard *.cc)

make:
	g++ $(CC_FILES) -o s -g -lrt -Wall
	sudo setcap cap_sys_nice=ep ./s
	taskset -c 0 ./s 500 5 100000 SCHED_RR

fifo:
	g++ $(CC_FILES) -o s -g -lrt -Wall
	sudo setcap cap_sys_nice=ep ./s
	taskset -c 0 ./s 500 5 100000 SCHED_FIFO

rr:
	g++ $(CC_FILES) -o s -g -lrt -Wall
	sudo setcap cap_sys_nice=ep ./s
	taskset -c 0 ./s 500 1 100000 SCHED_RR

clean:
	rm -f *.o s
	clear