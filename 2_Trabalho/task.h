#ifndef TASK_H
#define TASK_H

#include "timer.h"

class Task {
public:
    Task(unsigned int period, int priority, unsigned long load, unsigned int count) {
        _period = period;
        _priority = priority;
        _load = load;
        _count = count;

        sigemptyset(&set);
        sigaddset(&set, SIGALRM);
    }

    void run() {
        int sig = 0;
        unsigned int i = 0;
        while (!sigwait(&set, &sig) && i++ < _count) {
            dummyFunction(0);
        }
    }

private:
    static void dummyFunction(int a = 0) {
        for (unsigned int i = 0; i < _load * 1000; ++i);
        _timer->showTime();
    }

private:
    unsigned int _period;
    int _priority;
    unsigned int _count;
    sigset_t set;

public:
    static unsigned long _load;
    static Timer * _timer;
};

#endif