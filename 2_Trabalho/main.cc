#include "timer.h"
#include "task.h"

#define REPETITIONS 15 // Number of repetitions to stop program

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
        load = (unsigned long)atoi(argv[3]);
        isFIFO = (argv[4][6] == 'F');
    } else {
        std::cout << "Error: please specify every parameter \n[period ms, priority, load, scheduler (SCHED_FIFO or SCHED_RR)]\n";
        return 0;
    }
    std::cout << "\nSettings:\n    Period: " << period << "\n    Priority: " << priority << "\n    Load: " << load << "\n    Scheduler: " << argv[4] << "\n\n";

    // Starts execution
    Task::_timer = new Timer(period);
    
    Task * task = new Task(period, priority, load, REPETITIONS);
    task->run();

    delete Task::_timer;
    delete task;

    return 0;
}