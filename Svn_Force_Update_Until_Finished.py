#!/usr/bin/env python\

from subprocess import call
import logging
import datetime

svn_cmd = "svn"
update_arg = "up"
cleanup_arg = "cleanup"
tries_before_giving_up = 75

def main():
    configure_Logging()
    
    number_of_tries_so_far = 1
    is_finished = False
    
    time_start = datetime.datetime.now()
    
    while(number_of_tries_so_far <= tries_before_giving_up and not is_finished):
        logging.info("Cleaning up!")
        call([svn_cmd, cleanup_arg])
        status = call([svn_cmd, update_arg])
        logging.debug(status)
    
        if status != 0:
            logging.error('Error!: Status was different from Zero: %s', str(status))
            logging.warn('Tries so far: %s', str(number_of_tries_so_far))
            number_of_tries_so_far += 1
        else:
            is_finished = True
            print("We're done after %s tries" % str(number_of_tries_so_far))
    
    if(number_of_tries_so_far > tries_before_giving_up):
        logging.warn("Exiting because the max number of tries was reached!: %s", str(number_of_tries_so_far))
    
    time_finish = datetime.datetime.now()
    execution_time = time_finish - time_start
    
    logging.info("Start time: %s", str(time_start))
    logging.info("Finish time: %s", str(time_finish))
    print("Total execution time: %s" % str(execution_time))
        
def configure_Logging():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Ready to DEBUG!")
    
if __name__ == "__main__":
    main()