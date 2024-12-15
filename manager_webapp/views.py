from django.shortcuts import render

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def home(request):
    logger.debug("Home view was called")
    return HttpResponse("Helo")