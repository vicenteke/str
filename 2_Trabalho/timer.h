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
    // estrutura que define um tratador de sinal
    struct sigaction action;

    // // estrutura de inicialização to timer
    // struct itimerval timer;
    unsigned int _period;
    Function *_handler;

    timer_t timer;
    struct sigevent sigev;
    struct itimerspec itspec;
};

#endif
