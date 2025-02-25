import time
import logging

logger = logging.getLogger(__name__)

class PerformanceLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()

        duration = (end_time - start_time) * 1000  # Convert to milliseconds
        logger.info(f"Request: {request.path} | Time Taken: {duration:.2f} ms")

        return response
