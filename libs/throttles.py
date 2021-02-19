from rest_framework.throttling import UserRateThrottle


class SmartiaRateLimit(UserRateThrottle):
    scope = 'gateway'
