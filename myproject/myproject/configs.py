from decouple import config


class WebhookConfig:
    webhook_url = config('WEBHOOK_URL', default='http://localhost:8000/api/webhook/')
