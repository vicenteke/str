#include "timer.h"

Timer::Timer(const unsigned int period, const Function * handler) {

    _period = period;
    _handler = handler;

    // Sets "handler" as handler for signal SIGALRM
    setHandler(handler);

    // Creates timer
    sigev.sigev_notify = SIGEV_SIGNAL;
    sigev.sigev_signo = SIGALRM;
    sigev.sigev_value.sival_ptr = &timer;
    timer_create(CLOCK_REALTIME, &sigev, &timer);

    // Configures alarm timer
    reset();

}

void Timer::reset() {

    // Restarts timer counting
    itspec.it_value.tv_sec = 0;
    itspec.it_value.tv_nsec = _period * 1000000;
    itspec.it_interval.tv_sec = 0;
    itspec.it_interval.tv_nsec = _period * 1000000;
    timer_settime(timer, 0, &itspec, NULL);
}

void Timer::setHandler(const Function * handler) {
    action.sa_handler = handler;
    sigaction(SIGALRM, &action, NULL);
}

void Timer::showTime() {
    timer_gettime(timer, &itspec);
    std::cout << (_period - (int)(itspec.it_value.tv_nsec / 1000000)) << "ms\n";
}
