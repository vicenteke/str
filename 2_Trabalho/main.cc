#include "timer.h"
#include "task.h"
#include <sched.h>
#include <cstring>

#define REPETITIONS 25 // Number of repetitions to stop program

int main(int argc, char const *argv[])
{
    unsigned int period;
    int priority;
    unsigned long load;
    bool isFIFO;

    // Gets command line parameters
    if (argc > 4) {
        period = (unsigned int)atoi(argv[1]);
        priority = atoi(argv[2]);

        if (priority < 1 || priority > 99) {
            std::cout << "Priority should be between 1 - 99, set to 5...\n";
            priority = 5;
        }

        load = (unsigned long)atoi(argv[3]);
        isFIFO = (argv[4][6] == 'F');
    } else {
        std::cout << "Error: please specify every parameter \n[period ms, priority, load, scheduler (SCHED_FIFO or SCHED_RR)]\n";
        return 0;
    }
    std::cout << "\nSettings:\n    Period: " << period << "\n    Priority: " << priority << "\n    Load: " << load << "\n    Scheduler: " << argv[4] << "\n\n";

    // Set scheduler
    int policy = (isFIFO) ? SCHED_FIFO : SCHED_RR;
    sched_param param;
    sched_getparam(0, &param);
    param.sched_priority = priority;

    if(sched_setscheduler(0, policy, &param) == -1) {
        std::cout << "Failed to set scheduler options, running on default...\n" << std::strerror(errno) << std::endl;
    }
    // } else {
    //     if(!isFIFO) {
    //         std::cout << "    RR Interval: " << sched_rr_get_interval() << '\n';
    //     }
    //     std::cout << '\n';
    // }

    // Starts execution
    Task::_timer = new Timer(period);
    
    Task * task = new Task(period, priority, load, REPETITIONS);
    task->run();

    delete Task::_timer;
    delete task;

    return 0;
}