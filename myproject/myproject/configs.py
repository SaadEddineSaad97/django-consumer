from decouple import config


class WebhookConfig:
    webhook_url = config('WEBHOOK_URL', default='0.0.0.0:8000/api/webhook')
