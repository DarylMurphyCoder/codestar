import logging
import traceback

class LogExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            logger = logging.getLogger("django")
            logger.error(f"Unhandled exception: {e}\n{traceback.format_exc()}")
            raise
        return response