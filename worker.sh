#!/bin/bash
#arranca el  worker 
cd /var/www/2run/
celery -A buscarut worker -l info
