import time

class PerformanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        execution_time = time.time() - start_time

        # Add execution time in the response headers (useful for APIs)
        response["X-Execution-Time"] = f"{execution_time:.4f} sec"
        
        return response
