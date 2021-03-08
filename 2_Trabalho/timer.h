#ifndef timer_h
#define timer_h

#include <iostream>
#include <signal.h>
#include <sys/time.h>

class Timer
{
public:
    typedef void (Function)(int);

    Timer(const unsigned int period, const Function * handler = &printLostDeadline); //period in us
    void reset();
    void setHandler(const Function * handler = &printLostDeadline);
    void showTime();

private:
    static void printLostDeadline(int i) {
        std::cout << "--> Deadline Perdido!!\n";
    }

private:
    struct sigaction action;
    struct sigevent sigev;
    
    timer_t timer;
    struct itimerspec itspec;
    unsigned int _period;
    Function *_handler;
};

#endif
