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

        _timer = new Timer(period);

        sigemptyset(&set);
        sigaddset(&set, SIGALRM);
    }

    ~Task() {
        delete _timer;
    }

    void run() {
        int sig = 0;
        unsigned int i = 0;
        while (!sigwait(&set, &sig) && i++ < _count) {
            dummyFunction();
        }
    }

private:
    void dummyFunction() {
        for (unsigned int i = 0; i < _load * 1000; ++i);
        _timer->showTime();
    }

private:
    unsigned int _period;
    int _priority;
    unsigned int _count;
    sigset_t set;
    unsigned long _load;
    Timer * _timer;
};

#endif