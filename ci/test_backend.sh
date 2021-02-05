#!/bin/bash
docker-compose -f docker/compose/test.yml run projeto01 unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
